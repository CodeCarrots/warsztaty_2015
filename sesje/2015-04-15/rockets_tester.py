import random

from rockets import Rocket, STATES


DEF_THRUSTS = [100, 200, 500]


def test_rocket_class(cls, parental_class):
    if not issubclass(cls, parental_class):
        raise ValueError(cls, 'is not derived from', parental_class)


def test_rocket_instance(rocket, prev_thrust, clean_obj=True):
    # test ciagu
    if not hasattr(rocket, 'get_thrust'):
        raise NotImplementedError('No get_thrust() method at', rocket, '!')
    curr_thrust = rocket.get_thrust()
    if curr_thrust <= 0 or curr_thrust <= prev_thrust:
        raise ValueError('Bad thrust (=', curr_thrust, ') at', rocket, '!')
    print('Thrust - OK at', rocket)

    # test stanow
    if not hasattr(rocket, 'get_state'):
        raise NotImplementedError('No get_state() method at', rocket, '!')
    if not hasattr(rocket, 'set_state'):
        raise NotImplementedError('No set_state() method at', rocket, '!')
    for idx, state in enumerate(STATES):
        if idx == 0:
            if clean_obj and rocket.get_state() != STATES[0]:
                raise ValueError('Bad start state at', rocket, '!')
            elif rocket.get_state() not in STATES:
                raise ValueError('Bad transition state at', rocket, '!')
            continue
        prev_state = rocket.get_state()
        rocket.set_state(state)
        curr_state = rocket.get_state()
        if curr_state not in [prev_state, state] or \
            (clean_obj and STATES.index(prev_state) != (STATES.index(state) - 1)) or \
            STATES.index(curr_state) not in [STATES.index(prev_state), STATES.index(state)]:
            raise ValueError('Bad state transition:', curr_state, 'not in', [prev_state, state])
        for random_state in random.sample(STATES[:idx], idx):
            rocket.set_state(random_state)
            test_state = rocket.get_state()
            if test_state != curr_state:
                raise ValueError('Bad state transition:', test_state, 'not in', [prev_state, curr_state])
    print('States - OK at', rocket)
    return curr_thrust


def test_rockets(classes, instances):
    prev_thrust = 0
    for idx, cls in enumerate(classes):
        parental_class = Rocket if idx in [0, 2] else classes[idx - 1]
        test_rocket_class(cls, parental_class)
        print('Class - OK at', cls)
        try:
            rocket = cls(DEF_THRUSTS[idx])
        except TypeError:
            rocket = cls()
        prev_thrust = test_rocket_instance(rocket, prev_thrust)
    prev_thrust = 0
    for idx, rocket in enumerate(instances):
        if not isinstance(rocket, classes[idx]):
            raise ValueError(rocket, 'is not a', classes[idx], 'object')
        parental_class = Rocket if idx in [0, 2] else classes[idx - 1]
        test_rocket_class(rocket.__class__, parental_class)
        prev_thrust = test_rocket_instance(rocket, prev_thrust, clean_obj=False)
        print('Instance - OK at', rocket)

