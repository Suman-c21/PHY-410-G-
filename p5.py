#!/usr/bin/env python
# coding: utf-8

# In[46]:


'''Python Script to calculate the initial velocity of the bullet and solving the problem to calcualte the final height 
after rebounding.'''

import numpy as np                  # Import python Libraries.
d = 100.0
g = 9.8                             # Acceleration due to gravity (m/s^2).       
ux = 472.0                          # Initial velocity.
Y2 = 0
while(Y2 < 50.0 or Y2 > 50.2):
    t =  d/ux                        # Time taken by bullet (s).
    uy = 0.0                         # Initial velocity (m/s).
    vy = uy + g*t                    # vertical component of velocity (m/s).
    h = uy*t + 0.5*g*t**2            # Height from ground level in meter (m). 
    y1 = 1.3 - h                     # Height the bullet impact in meter (m).
    v = np.sqrt((ux)**2. + (vy)**2.) # Total velocity (m/s).
    m= 4.2e-3                        # Mass of bullet in (kg).
    kb = 0.5*m*(v**2.)               # Kinetic energy before wall in Joules (J).
    ka = 0.22*kb                     # kinetic energy after wall in Joules(J).
    V = np.sqrt(2.*ka/m)             # Velocity after  wall collision (m/s).
    T = d/V                          # Returning time after collision (s).
    h1 = 0.5*g*T**2.                 # Height from ground level after (m).
    Y2 = (y1-h1)*100.                # Height at impact after returning (cm).

if (50.0 < Y2 < 50.2):
    print('The bullet hits the boy in the given range and the velocity is %1.1f m/s.'%vx )
else:
    print ('The velocity  %1.1f m/s is too low to hit the boy in the given range.' %vx)
    ux += 0.1


# In[ ]:





# In[ ]:




