from app.models.api_response import APIResponse
from app.models.chat_message import ChatMessage
from app.models.invoice import Invoice
from app.models.receipt import Receipt
from app.models.user_profile import UserProfile


def user_profile_demo():
    print("\n" + "=" * 60)
    print("USER PROFILE DEMO")
    print("=" * 60)

    user = UserProfile(
        name="Chandan Yadav",
        email="chandan@gmail.com",
        age=24,
        city="Mumbai",
        phone="9876543210",
    )

    response = APIResponse(
        success=True,
        message="User fetched successfully",
        data=user,
    )

    print(response.model_dump_json(indent=4))


def receipt_demo():
    print("\n" + "=" * 60)
    print("RECEIPT DEMO")
    print("=" * 60)

    receipt_data = {
        "store_name": "DMart",
        "purchase_date": "2026-07-09T10:30:00",
        "items": [
            {
                "name": "Milk",
                "quantity": 2,
                "price": "40.50",
            },
            {
                "name": "Bread",
                "quantity": 1,
                "price": "35.00",
            },
        ],
        "total": "116.00",
    }

    receipt = Receipt.model_validate(receipt_data)

    response = APIResponse(
        success=True,
        message="Receipt processed successfully",
        data=receipt,
    )

    print(response.model_dump_json(indent=4))


def invoice_demo():
    print("\n" + "=" * 60)
    print("INVOICE DEMO")
    print("=" * 60)

    invoice = Invoice(
        customer_name="Chandan Yadav",
        customer_email="chandan@gmail.com",
        amount="4999.99",
    )

    response = APIResponse(
        success=True,
        message="Invoice created successfully",
        data=invoice,
    )

    print(response.model_dump_json(indent=4))


def chat_demo():
    print("\n" + "=" * 60)
    print("CHAT MESSAGE DEMO")
    print("=" * 60)

    chat = ChatMessage(
        role="assistant",
        content="Hello Chandan! Welcome to Pydantic.",
        token_count=18,
    )

    response = APIResponse(
        success=True,
        message="Chat generated successfully",
        data=chat,
    )

    print(response.model_dump_json(indent=4))


def validation_demo():
    print("\n" + "=" * 60)
    print("VALIDATION ERROR DEMO")
    print("=" * 60)

    bad_user = {
        "name": "A",
        "email": "wrong-email",
        "age": 10,
    }

    try:
        UserProfile.model_validate(bad_user)

    except Exception as e:
        print(e)


def main():
    user_profile_demo()
    receipt_demo()
    invoice_demo()
    chat_demo()
    validation_demo()


if __name__ == "__main__":
    main()