from datetime import timedelta, datetime
from sqlalchemy.orm import Session

from sqlalchemy import extract
from src.database.models import Contact
from src.schemas import ContactBase


async def search_contacts(name: str, fullname: str, email: str, db: Session):

    if name:
        contact = db.query(Contact).filter_by(name=name).all()
        return contact
    if fullname:
        contact = db.query(Contact).filter_by(fullname=fullname).all()
        return contact
    if email:
        contact = db.query(Contact).filter_by(email=email).all()
        return contact


async def search_birthday(db: Session):
    today = datetime.today()
    end_date = today + timedelta(days=7)
    contacts = db.query(Contact).filter(
            ((extract('month', Contact.birthday) == today.month) & (extract('day', Contact.birthday) >= today.day)) |
            ((extract('month', Contact.birthday) == end_date.month) & (
                    extract('day', Contact.birthday) <= end_date.day))
        ).all()

    return contacts


async def get_contacts(offset: int, limit: int, db: Session):
    return db.query(Contact).offset(offset).limit(limit).all()


async def get_contact(contact_id: int, db: Session):
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactBase, db: Session):
    contact = Contact(name=body.name,
                      fullname=body.fullname,
                      email=body.email,
                      phone_number=body.phone_number,
                      birthday=body.birthday,
                      description=body.description)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactBase, db: Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = body.name
        contact.fullname = body.fullname
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birthday = body.birthday
        contact.description = body.description
    db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def get_contact_by_email(email: str, db: Session):
    contact = db.query(Contact).filter_by(email=email).first()
    return contact
