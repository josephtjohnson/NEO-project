"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name, diameter, hazardous, approaches = [], **info):
        """Create a new `NearEarthObject`.
        :param designation: The designation for a near earth object.
        :param name: The name for a near earth object.
        :param diameter: The diameter of a near earth object.
        :param hazardous: A boolean value indicating if a near earth object is hazardous.
        :param approaches: A collection of close approach events for a near earth object.        
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self.designation = str(designation)
        if name == '':
            self.name = None
        else:
            self.name = name
        if diameter == '':
            self.diameter = float('nan')
        else:
            self.diameter = float(diameter)
        self.hazardous = hazardous
        self.approaches = list(approaches)

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO. Scenario for name undefined."""

        if self.name is not None:
            return self.designation + ' ' + self.name
        else:
            return self.designation
            
    def __str__(self):
        """Return `str(self)`. Scenario for hazard Y/N accounted for."""

        if self.hazardous is True:
            return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and is potentially hazardous."
        else:
            return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and is not potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, time, distance, velocity, neo=None, **info):
        """Create a new `CloseApproach`.
        :param designation: The designation for a near earth object.
        :param time: The close approach event time.
        :param distance: The distance from earth that a close approach event occurred.
        :param velocity: The speed at which a near earth object was travling during a close approach event.
        :param neo: The a collection of properties for a near earth object returned from NearEarthObject.
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        
        self._designation = str(designation)
        self.time = cd_to_datetime(time)  
        self.distance = float(distance) if distance else float('nan')
        self.velocity = float(velocity) if velocity else float('nan')
        self.neo = None
    
    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """

        return datetime_to_str(self.time)
    
    def __str__(self):
        """Return `str(self)`."""
        
        return f"A close approach event ocurred on {self.time_str} for '{self.neo.fullname}' at a distance of {self.distance:.2f} au with a velocity of {self.velocity:.2f} km/s. "

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
