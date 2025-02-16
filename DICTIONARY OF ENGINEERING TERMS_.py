print("ENGINEERING TERMINOLOGIES DICTIONARY")
#PROCESS: List of Engineering terms with definitions.
DATA={
"ALGORITHM":"A step-by-step procedure or formula for solving a problem, often used in computer programming and automation.",
"BEAM":"A structural element that primarily resists loads applied laterally to its axis, commonly used in construction.",
"COMPUTER AIDED DESIGN":"The use of computer software to create, modify, analyze, or optimize designs in engineering and architecture.",
"COMPRESSIVE STRENGTH":"The capacity of a material to withstand axial compressive forces without failing.",
"CIRCUIT":"A complete, closed path through which electric current can flow.",
"CORROSION":"The gradual destruction of materials (usually metals) by chemical or electrochemical reaction with their environment.",
"DIELECTRIC":"A material that does not conduct electricity but can store electrical energy through polarization.",
"EFFICIENCY":"The ratio of useful output to total input in any system, often expressed as a percentage.",
"FINITE ELEMENT ANALYSIS":"A numerical method for predicting how a product reacts to real-world forces, vibration, heat, and other physical effects.",
"FLUID DYNAMICS":"The study of the behavior of fluids (liquids and gases) in motion.",
"GEAR":"A rotating mechanical component with cut teeth or cogs that mesh with another gear to transmit torque.",
"HVAC":"(Heating, Ventilation, and Air Conditioning).A system used to provide heating, cooling, and air quality control in buildings.",
"INDUCTOR":"An electrical component that stores energy in a magnetic field when electric current flows through it.",
"KINEMATICS":"The study of motion without considering the forces that cause it.",
"LOAD":"The external force or forces applied to a structure or component.",
"MECHATRONIX":"An interdisciplinary branch of engineering that combines mechanical, electrical, computer, and control engineering.",
"NANOTECHNOLOGY":"The manipulation of matter on an atomic or molecular scale, typically below 100 nanometers.",
"OHM'S LAW":"A fundamental principle of electrical circuits stating that voltage equals current multiplied by resistance (V = I × R).",
"PNEUMATICS":"The use of compressed air to perform mechanical work.",
"POWER":"The rate at which work is done or energy is transferred, measured in watts.",
"RESISTOR":"An electrical component that limits or regulates the flow of electric current in a circuit.",
"ROBOTICS":"The design, construction, operation, and use of robots for various applications.",
"SHEAR FORCE":"A force that acts parallel to a surface, causing layers to slide relative to each other.",
"STATIC EQUILIBRIUM":"A state in which a structure remains at rest with no net force or moment acting on it.",
"STRESS":"The internal force per unit area within a material, resulting from external loads.",
"STRUCTURAL INTEGRITY":"The ability of a structure to withstand its intended load without failure.",
"THERMODYNAMICS":"The study of heat, energy, and work and their interactions.",
"TORQUE":"A measure of the force that can cause an object to rotate about an axis.",
"VALVE":"A mechanical device that controls the flow of fluids or gases by opening, closing, or partially obstructing passageways.",
"WELDING":"The process of joining materials, usually metals or thermoplastics, by melting and fusing them together."
}
#INPUT:The user is prompted to enter a word related to engineering terminology.
while True:
  a = input("Type your word:")
     #OUTPUT:If the input term exists in the dictionary, the program prints the corresponding engineering definition.
  print(DATA[a])
