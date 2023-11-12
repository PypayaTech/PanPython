from pan_python.engine import Engine
from pan_python.move_step import MoveStep
from pan_python.wait_step import WaitStep


def main():
    engine = Engine("timeline.png", init_cam_pos=(-200, 400))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(1, 200, 355, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 350, -355, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 450, 355, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 450, -355, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 450, 355, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 450, -785, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 450, 810, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 0, 510, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 450, -1320, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 250, 805, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 250, -385, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 450, 385, is_relative=True))
    engine.add_step(WaitStep())
    engine.add_step(MoveStep(0.5, 450, -375, is_relative=True))
    engine.add_step(WaitStep())
    engine.run(start_index=0)


if __name__ == "__main__":
    main()
