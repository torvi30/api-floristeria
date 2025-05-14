from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from orders.model import Order, OrderDetail
from orders.schema import OrderCreate, OrderResponse, OrderUpdate
from products.model import Product

router = APIRouter(prefix="/orders", tags=["Orders"])

# Crear un pedido
@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    total_price = 0
    order_details = []
    for detail in order.order_detail:
        product = db.query(Product).filter(Product.id == detail.product_id).first()
        if not product or product.stock < detail.quantity:
            raise HTTPException(status_code=400, detail="Stock insuficiente para el producto")
        product.stock -= detail.quantity
        subtotal = detail.quantity * detail.unit_price
        total_price += subtotal
        order_details.append(OrderDetail(**detail.dict(), subtotal=subtotal))

    db_order = Order(
        customer_name=order.customer_name,
        customer_phone=order.customer_phone,
        total_price=total_price,
        status=order.status,
        order_detail=order_details,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Obtener todos los pedidos
@router.get("/", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

# Obtener un pedido por ID
@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return order

# Actualizar un pedido
@router.put("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, updated_order: OrderUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    if updated_order.order_detail:
        # Revertir el stock de los productos del pedido actual
        for detail in order.order_detail:
            product = db.query(Product).filter(Product.id == detail.product_id).first()
            product.stock += detail.quantity

        # Actualizar los detalles del pedido
        order.order_detail.clear()
        total_price = 0
        for detail in updated_order.order_detail:
            product = db.query(Product).filter(Product.id == detail.product_id).first()
            if not product or product.stock < detail.quantity:
                raise HTTPException(status_code=400, detail="Stock insuficiente para el producto")
            product.stock -= detail.quantity
            subtotal = detail.quantity * detail.unit_price
            total_price += subtotal
            order.order_detail.append(OrderDetail(**detail.dict(), subtotal=subtotal))
        order.total_price = total_price

    for key, value in updated_order.dict(exclude_unset=True).items():
        if key != "order_detail":
            setattr(order, key, value)

    db.commit()
    db.refresh(order)
    return order

# Eliminar un pedido
@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    # Revertir el stock de los productos del pedido
    for detail in order.order_detail:
        product = db.query(Product).filter(Product.id == detail.product_id).first()
        product.stock += detail.quantity

    db.delete(order)
    db.commit()
    return {"message": "Pedido eliminado"}
