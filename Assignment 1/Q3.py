class Package:
    def __init__(self, packageId, weight):
        self.packageId = packageId
        self.weightInKg = weight


class Drone:
    def __init__(self, id, maxLoad):
        self.droneId = id
        self.maxLoadInKg = maxLoad
        self.__status = "idle"
        self.package = None
        self.timer = 0

    def setStatus(self, newStatus):
        newStatus = newStatus.lower()
        if newStatus in ("idle", "delivering", "charging"):
            self.__status = newStatus
        else:
            print("invalid status input")

    def getStatus(self):
        return self.__status

    def assignPackage(self, packageObj):
        if self.getStatus() != "idle":
            print(f"Drone {self.droneId} not idle , can not assign the package {packageObj.packageId}")
            return False
        
        if packageObj.weightInKg > self.maxLoadInKg:
            print(f"Package too heavy for Drone {self.droneId}")
            return False
        
        self.package = packageObj
        self.setStatus("delivering")
        self.timer = 2
        print(f"Drone {self.droneId} assigned to package {packageObj.packageId}")
        return True

    def update(self):
        current = self.getStatus()

        if current == "delivering":
            self.timer -= 1
            if self.timer <= 0:
                self.package = None
                self.setStatus("charging")
                self.timer = 1

        elif current == "charging":
            self.timer -= 1
            if self.timer <= 0:
                self.setStatus("idle")


class FleetManager:
    def __init__(self):
        self.drones = {}
        self.pendingPackages = []

    def addDrone(self, droneObj):
        self.drones[droneObj.droneId] = droneObj

    def addPackage(self, packageObj):
        self.pendingPackages.append(packageObj)

    def dispatchJobs(self):
        for drone in self.drones.values():
            if drone.getStatus() == "idle" and self.pendingPackages:
                pkg = self.pendingPackages.pop(0)
                allocated = drone.assignPackage(pkg)
                if not allocated:
                    self.pendingPackages.insert(0, pkg)

    def simulationTick(self):
        print("-Simulation Ticks-")
        for drone in self.drones.values():
            drone.update()
            print(f"Drone {drone.droneId} -> status: {drone.getStatus()}")

manager = FleetManager()

d1 = Drone("D1", 10)
d2 = Drone("D2", 5)
manager.addDrone(d1)
manager.addDrone(d2)

p1 = Package("P1", 4)
p2 = Package("P2", 6)
p3 = Package("P3", 8)
manager.addPackage(p1)
manager.addPackage(p2)
manager.addPackage(p3)

manager.dispatchJobs()
manager.simulationTick()
manager.simulationTick()
manager.simulationTick()
manager.simulationTick()
