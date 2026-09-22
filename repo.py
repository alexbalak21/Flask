from db import db, Item

class ItemRepository:
    @staticmethod
    def create(name, price):
        new_item = Item(name=name, price=price)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def get_all():
        return Item.query.all()

    @staticmethod
    def get_by_id(item_id):
        return Item.query.get(item_id)

    @staticmethod
    def update(item_id, name=None, price=None):
        item = Item.query.get(item_id)
        if not item:
            return None
            
        if name is not None:
            item.name = name
        if price is not None:
            item.price = price
            
        db.session.commit()
        return item

    @staticmethod
    def delete(item_id):
        item = Item.query.get(item_id)
        if not item:
            return False
            
        db.session.delete(item)
        db.session.commit()
        return True
