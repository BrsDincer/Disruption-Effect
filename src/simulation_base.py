from util_main import CLASSINIT,NULL,ERROR,DOCUMENTATION,PROCESS,ERRORMODULE
from util_main import ErrorProbability,PopulateEnvironment,ApplyEnvironmentRules,RunDisruption,ReturnFontConfiguration
import pygame,numpy as np,random,time

class SimulationBase(object):
    """
    A base class for running a SimulationBase in a 2D grid environment.
    
    Attributes:
        size (int): The size of the simulation grid.
        environment (numpy.ndarray): A 2D array representing the simulation environment.
        cellColor (tuple): The color of active cells in the simulation.
        gridColor (tuple): The color of the grid lines in the simulation.
        textColor (tuple): The color used for text in the simulation.
        active (int): Counter for active cells.
        deactive (int): Counter for deactive cells.
        disruption (int): Counter for the number of disruptions occurred.
        xdim (int): The x-dimension of each cell in pixels.
        ydim (int): The y-dimension of each cell in pixels.
        stopTime (float): The duration for which the simulation will run.
        maxError (float): The maximum error probability in the simulation.
        defaultCell (int): The default number of cells to initialize in the environment.
    
    Methods:
        __str__: Returns a string representation of the simulation.
        __call__: Placeholder method, currently returns None.
        __getstate__: Method for error handling.
        __repr__: Returns the documentation of the class.
        Draw: Renders the simulation environment on the screen.
        Initialize: Initializes and runs the simulation.
    """
    def __init__(self)->CLASSINIT:
        self.size = 20
        self.environment = np.zeros((self.size,self.size))
        self.cellColor = (0,255,0)
        self.gridColor = (10,10,10)
        self.textColor = (255,255,255)
        self.active = 0
        self.deactive = 0
        self.disruption = 0
        self.xdim = 20
        self.ydim = 20
        self.stopTime = 13.7
        self.maxError = 0.1
        self.defaultCell = 1000
    def __str__(self)->str:
        return "Simulation - Main(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return SimulationBase.__doc__
    def Draw(self,screen:CLASSINIT,pointShift:int=10)->PROCESS:
        for x in range(self.size):
            for y in range(self.size):
                rectangle = pygame.Rect(
                        y*(self.size+pointShift),
                        x*(self.size+pointShift),
                        (self.size+pointShift),
                        (self.size+pointShift)
                    )
                color = self.cellColor if self.environment[x,y] == 1 else self.gridColor
                pygame.draw.rect(screen,color,rectangle)
    def Initialize(self)->PROCESS:
        pygame.init()
        startTime = time.time()
        surface = pygame.display.set_mode(
                (
                    self.xdim*self.size,
                    self.ydim*self.size
                )
            )
        pygame.display.set_caption("Disruption Schema-Simulation")
        font = pygame.font.Font(None,15)
        timeEngine = pygame.time.Clock()
        ticks = pygame.time.get_ticks()
        self.environment = PopulateEnvironment(environment=self.environment,
                                               objectCount=self.defaultCell,
                                               size=self.size)
        errorProbability = ErrorProbability(environment=self.environment,
                                            size=self.size,
                                            maxError=self.maxError)
        while True and ((time.time()-startTime) < self.stopTime):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    return
            surface.fill(self.gridColor)
            self.environment = ApplyEnvironmentRules(environment=self.environment,
                                                     size=self.size)
            if random.random() < errorProbability:
                self.environment,self.disruption = RunDisruption(environment=self.environment,
                                                                      size=self.size,
                                                                      disruptionCount=self.disruption)
            else:
                pass
            self.Draw(screen=surface)
            self.active = (self.environment == 1).sum()
            self.deactive = (self.environment == 0).sum()
            endTime = pygame.time.get_ticks() - ticks
            errorInfo = f"ERROR PROBABILITY - DEPENDS {str(self.defaultCell)} OBJECTS: {str(round(errorProbability,4))}"
            timeInfo = f"TIME (sec): {str(endTime/1000)}"
            activeInfo = f"ACTIVE (cell): {str(self.active)}"
            deactiveInfo = f"DEACTIVE (cell): {str(self.deactive)}"
            disruptionInfo = f"DISRUPTION (total): {str(self.disruption)}"
            errorOut = ReturnFontConfiguration(font,errorInfo,self.textColor)
            timeOut = ReturnFontConfiguration(font,timeInfo,self.textColor)
            activeOut = ReturnFontConfiguration(font,activeInfo,self.textColor)
            deactiveOut = ReturnFontConfiguration(font,deactiveInfo,self.textColor)
            disruptionOut = ReturnFontConfiguration(font,disruptionInfo,self.textColor)
            surface.blit(errorOut,(12,self.xdim+195))
            surface.blit(timeOut,(12,self.xdim+215))
            surface.blit(activeOut,(12,self.xdim+235))
            surface.blit(deactiveOut,(12,self.xdim+255))
            surface.blit(disruptionOut,(12,self.xdim+275))
            timeEngine.tick(10)
            pygame.display.update()
        pygame.quit()
            
if __name__ == "__main__":
    SimulationBase().Initialize()
            
            
        
        