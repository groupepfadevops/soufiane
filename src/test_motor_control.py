import unittest
from motor_control import Motor

class TestMotor(unittest.TestCase):
    def test_rotate_clockwise(self):
        motor = Motor()
        motor.rotate('clockwise')
        self.assertEqual(motor.direction, 'clockwise')

    def test_rotate_counterclockwise(self):
        motor = Motor()
        motor.rotate('counterclockwise')
        self.assertEqual(motor.direction, 'counterclockwise')

    def test_stop(self):
        motor = Motor()
        motor.rotate('clockwise')
        motor.stop()
        self.assertEqual(motor.direction, 'stopped')

    def test_invalid_direction(self):
        motor = Motor()
        with self.assertRaises(ValueError):
            motor.rotate('invalid')

if __name__ == '__main__':
    unittest.main()
