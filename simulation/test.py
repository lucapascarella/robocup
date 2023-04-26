import pybullet as p
import pybullet_data as pd

from multiprocessing import Process
from qibullet import SimulationManager
from simulator import Robot

from players.simple_player import SimplePlayer

class TestSimulator:
    def __init__(self, Player):
        # Initialize the simulation manager
        self.manager = SimulationManager()
        self.client = self.manager.launchSimulation(gui=True, auto_step=False)

        # Initialize the player
        self.player = Player()
        self.robot = Robot(self.manager.spawnNao(self.client, 
            [0,0,0,0], [0, 0, 0, 1],
            spawn_ground_plane=True))

        self.player.setQueues(self.robot.request_queue, self.robot.frame_queue, self.robot.sensor_queue)

        p.setAdditionalSearchPath("./resources/objects")
        p.loadURDF(
            "soccerball.urdf",
            basePosition=[1, 0, 0],
            globalScaling=0.15,
            physicsClientId=self.client)

    def run(self):
        # Start the player process
        proc = Process(target=self.player.behave)
        proc.start()

        while True:
            try:
                if not self.robot.request_queue.empty():
                    request = self.robot.request_queue.get()
                    self.robot.handleRequest(request)

                self.manager.stepSimulation(self.client)
            except Exception as e:
                proc.kill()

if __name__ == "__main__":
    sim = TestSimulator(SimplePlayer)
    sim.run()