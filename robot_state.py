class RobotStateMachine:
    def __init__(self):
        self.state = 'pause'
        self.direction = 'stop'

    def update_state(self, new_state):
        if new_state == 'pause':
            self.direction = 'stop'
        elif new_state == 'fahren':
            self.direction = 'vorwaerts'
        elif new_state == 'error':
            self.direction = 'stop'
        else:
            print(f'Ungueltiger Zustand: {new_state}')
            return

        self.state = new_state

    def update_direction(self, new_direction):
        if self.state == 'pause':
            self.direction = 'stop'
        elif self.state == 'fahren':
            if new_direction in ['vorwaerts', 'rueckwaerts', 'links', 'rechts']:
                self.direction = new_direction
            else:
                print(f'Ungueltige Richtung: {new_direction}')
        elif self.state == 'error':
            self.direction = 'stop'
        else:
            print('Unbekannter Zustand')

    def print_state(self):
        print(f'Zustand: {self.state}, Richtung: {self.direction}')


# Example USAGE
#robot = RobotStateMachine()
#robot.update_state('fahren')
#robot.update_direction('vorwaerts')
#robot.print_state()
#robot.update_direction('diagonal')
#robot.print_state()
#robot.update_state('pause')
#robot.print_state()

# Augabe
#Zustand: fahren, Richtung: vorwaerts
#Ungueltige Richtung: diagonal
#Zustand: pause, Richtung: stop
