class Motor:
    def __init__(self):
        self.direction = 'stopped'

    def rotate(self, direction):
        if direction not in ['clockwise', 'counterclockwise']:
            raise ValueError('Invalid direction')
        self.direction = direction
        print(f'Motor rotating {self.direction}')

    def stop(self):
        self.direction = 'stopped'
        print('Motor stopped')

if __name__ == '__main__':
    motor = Motor()
    motor.rotate('clockwise')
    motor.stop()
