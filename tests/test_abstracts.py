from uuid import UUID
from abstracts.CartAbstract import CartItemAbstract, DbCartItemAbstract, CartAbstract
from unittest import TestCase
from commons.ENUMS import CartStatusEnum
from datetime import datetime

class CartAbstractTestCase(TestCase):
    def test_cart_abstract(self):
        # Arrange
        user_id = UUID("11111111-1111-1111-1111-111111111111")
        status = CartStatusEnum.ACTIVE
        ordered_at = datetime.now()
        # self.assertEqual(type(status), type('ACTIVE'))

        # Act
        cart = CartAbstract(user_id=user_id, ordered_at=ordered_at, status=status)

        # Assert
        self.assertEqual(cart.user_id, user_id)
        self.assertEqual(cart.status, status)
        self.assertEqual(cart.ordered_at, ordered_at)