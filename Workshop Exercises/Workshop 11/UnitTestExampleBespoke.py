# -*- coding: utf-8 -*-
"""
Author: Beth Wingate

This program converts data in miles per hour into either
      1) furlongs/fortnight, or
      2) m/s

We use a hand-written unit test types of unit tests.

"""
import numpy as np
import sys

#
# Define Functions
#
def Conversion(ConversionData, ConversionType):
    """

    This function converts data input in miles per hour into 
    either furlongs per fortnight or meters per second, or 
    perhaps other units in future versions of the code.

    Parameters
    ----------
    ConversionData : Array
        This is an array of data with units of miles per hour.
    ConversionType : String
        This is a string used to decide to convert miles per hour to either
        furlongs per fortnight or meters per second.

    Returns
    -------
    NewData: Array
       This is an array that holds the converted data

    """
    #
    # Create a new array to hold the converted data
    #
    NewData = np.copy(ConversionData) # The copy function allows changes to an array without changing the ori ginal array
    if ConversionType == 'FPF':
        #
        # Convert m/hr to f/f
        #
        # 1 mile/hour x 8 furlong/mile x 336 hours/fortnight = 
        #
        #
        ConversionFactor = 8.*336.
    elif ConversionType == 'METERSPS':
        #
        # Convert m/h to meters/s
        #
        # 1 mile/hour x 1609. meters/mile x 1/60 hour/minute x 1/60 minute/second 
        #
        #
        ConversionFactor = 1609./60./60.
    else:
        sys.exit("Program ended in function Conversion; with incorrect Conversion Type")
    for i in range(len(ConversionData)):
        NewData[i] = ConversionData[i]*ConversionFactor
        
    return NewData

def UnitTestC(ConversionFunction):
    """
        
    This function peforms unit tests for this program. It ensures that
    changes made to Conversion do not make errors to the following types:
        FPF
        METERSPS
        .
        .
        .

    Parameters
    ----------
    Conversion : Function
    This is a function that performs data conversions

    Returns
    -------
    None.

"""
    #
    # Check to make sure 
    #
    #  ConversionFunction(1,'FPF') = 2688.
    #
    #  and
    #
    #  ConversionFunction(1,'METERSPS') = 0.4469444444444444
    #
        
    epsilon = 1.e-8
    MyUnitTestArray =  np.ones(1)
        
    if np.abs(ConversionFunction(MyUnitTestArray,'FPF')-2688.) > epsilon:
        sys.exit("Unit test fails: 1*Conversionfactor for FPF returns the incorrect value")
    else:
        print("Unit test passes for MPH to FPF.")
        
    if np.abs(ConversionFunction(MyUnitTestArray,'METERSPS')-0.4469444444444444) > epsilon:
        sys.exit("Unit test fails: 1*Conversionfactor for METERSPS returns the incorrect value")
    else:
        print("Unit test passes for MPH to METERSPS.")
    
    
    return



#
#    Create a data set
#
Npoints = 60
SpeedArray = np.random.rand(Npoints)*100. # In Miles Per Hour

#
# Before we use the function, perform unit tests
#

UnitTestC(Conversion)

#
# Convert data, storing in new arrays
#
SpeedFurlongsPerFortnight = Conversion(SpeedArray,'FPF')
SpeedMetersPerSecond = Conversion(SpeedArray,'METERSPS')
#
#
