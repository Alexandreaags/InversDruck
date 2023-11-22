/*
This NanoJ Example Code is based on our experience with typical user requirements in a wide range
of industrial applications and is provided without guarantee regarding correctness and completeness.
It serves as general guidance and should not be construed as a commitment of Nanotec to guarantee its
applicability to the customer application without additional tests under the specific conditions
and   if and when necessary   modifications by the customer. 

The responsibility for the applicability and use of the NanoJ Example Code in a particular
customer application lies solely within the authority of the customer.
It is the customer's responsibility to evaluate, investigate and decide,
whether the Example Code is valid and suitable for the respective customer application, or not.
Defects resulting from the improper handling of devices and modules are excluded from the warranty.
Under no circumstances will Nanotec be liable for any direct, indirect, incidental or consequential damages
arising in connection with the Example Code provided. In addition, the regulations regarding the
liability from our Terms and Conditions of Sale and Delivery shall apply.
*/

//in this example the operationmode will be set to velocity mode, the state machine will be switched on and enabled with an input 

//1. Step: mapping the frequently used SDO s

map U16 ControlWord as output 0x6040:00
map S08 OperationMode as output 0x6060:00
map S16 TargetVelocity as output 0x6042:00
map U32 Inputs as input 0x60FD:00
map S32 Rasp as input 0x3320:01
map S32 ActualPosition as input 0x6064:00


#include "wrapper.h"
#define MAXSPEED 200

#define LOWEST_VELOCITY_BIT 50
#define MID_VELOCITY_BIT 275
#define HIGHEST_VELOCITY_BIT 500
#define OFFSET_BIT 10

//2. Step: call main function and set the speed and mode of operation

void user()
{
	
	bool bEnabled = false;   			// bool variable with name "bEnabled"
	int velocidade;
	//int vel_max = 500;	
	Out.OperationMode = 2;				// set the mode of operation to velocity mode (with mapping, line 5-8)
	//od_write(0x6060,0x00, 2);			// would also set the mode of operation to velocity mode (without mapping, line 5-8)
		
	Out.TargetVelocity = 0;				// set the target velocity to 200 rpm (basicvalue)(with mapping, line 5-8)
	//od_write(0x6042,0x00, 200);		// set the target velocity to 200 rpm (basicvalue)(without mapping, line 5-8)
		
	
//3. Step: switch on the state machine, use enable input
	
	Out.ControlWord = 0x6;				// switch to the "enable voltage" state
	do 	{
		yield();						// waiting for the next cycle (1ms)
		}
		while ( (od_read(0x6041, 0x00) & 0xEF) != 0x21);   // wait until drive is in state "enable voltage"
	
	// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0001
	

	while(true)							// endless loop
	{
		if(In.Rasp >= 0 && In.Rasp < (LOWEST_VELOCITY_BIT - OFFSET_BIT)) 										// Idle (0V)
			{	
			velocidade =  MAXSPEED * 0;

			Out.TargetVelocity = velocidade;

			if (bEnabled == false)		// motor is not running
				{
					bEnabled = true;		// then start the motor with...
					Out.ControlWord = 0x7;	// switch to the "switched on" state
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x23);   // wait until drive is in state "switched on"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0011				// waiting for the next cycle (1ms)
					Out.ControlWord = 0xF;	// switch to the "enable operation" state and starts the velocity mode
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x27);   // wait until drive is in state "operation enabled"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0111	
				}
			}
		else if(In.Rasp >= (LOWEST_VELOCITY_BIT - OFFSET_BIT) && In.Rasp < (LOWEST_VELOCITY_BIT + OFFSET_BIT)) 	// Go down at the fastest velocity
			{	
			velocidade =  MAXSPEED;

			Out.TargetVelocity = velocidade;

			if (bEnabled == false)		// motor is not running
				{
					bEnabled = true;		// then start the motor with...
					Out.ControlWord = 0x7;	// switch to the "switched on" state
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x23);   // wait until drive is in state "switched on"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0011				// waiting for the next cycle (1ms)
					Out.ControlWord = 0xF;	// switch to the "enable operation" state and starts the velocity mode
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x27);   // wait until drive is in state "operation enabled"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0111	
				}
			}			
		else if(In.Rasp >= (LOWEST_VELOCITY_BIT + OFFSET_BIT) && In.Rasp < MID_VELOCITY_BIT) 					// Go down at a variable speed
			{	
			//Percentage of velocity to be applied	
			velocidade = (In.Rasp - (LOWEST_VELOCITY_BIT + OFFSET_BIT))/(MID_VELOCITY_BIT - (LOWEST_VELOCITY_BIT + OFFSET_BIT))
			
			//Velocity to be outputed
			velocidade = (1 - velocidade) * MAXSPEED

			Out.TargetVelocity = velocidade;

			if (bEnabled == false)		// motor is not running
				{
					bEnabled = true;		// then start the motor with...
					Out.ControlWord = 0x7;	// switch to the "switched on" state
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x23);   // wait until drive is in state "switched on"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0011				// waiting for the next cycle (1ms)
					Out.ControlWord = 0xF;	// switch to the "enable operation" state and starts the velocity mode
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x27);   // wait until drive is in state "operation enabled"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0111	
				}
			}
		else if(In.Rasp >= MID_VELOCITY_BIT && In.Rasp < (HIGHEST_VELOCITY_BIT - OFFSET_BIT)) 					// Go up at a variable speed
			{	
			//Percentage of velocity to be applied	
			velocidade = (In.Rasp - MID_VELOCITY_BIT)/((HIGHEST_VELOCITY_BIT - OFFSET_BIT) - MID_VELOCITY_BIT)
			
			//Velocity to be outputed
			velocidade = velocidade * MAXSPEED * -1

			Out.TargetVelocity = velocidade;

			if (bEnabled == false)		// motor is not running
				{
					bEnabled = true;		// then start the motor with...
					Out.ControlWord = 0x7;	// switch to the "switched on" state
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x23);   // wait until drive is in state "switched on"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0011				// waiting for the next cycle (1ms)
					Out.ControlWord = 0xF;	// switch to the "enable operation" state and starts the velocity mode
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x27);   // wait until drive is in state "operation enabled"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0111	
				}
			}
		else if(In.Rasp >= (HIGHEST_VELOCITY_BIT - OFFSET_BIT))						 						// Go up at the fastest velocity
			{	
			velocidade =  MAXSPEED*-1;

			Out.TargetVelocity = velocidade;

			if (bEnabled == false)		// motor is not running
				{
					bEnabled = true;		// then start the motor with...
					Out.ControlWord = 0x7;	// switch to the "switched on" state
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x23);   // wait until drive is in state "switched on"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0011				// waiting for the next cycle (1ms)
					Out.ControlWord = 0xF;	// switch to the "enable operation" state and starts the velocity mode
					do 	{
							yield();						// waiting for the next cycle (1ms)
						}
						while ( (od_read(0x6041, 0x00) & 0xEF) != 0x27);   // wait until drive is in state "operation enabled"	
						// checking the statusword (0x6041) for the bitmask: xxxx xxxx x01x 0111	
				}
			}   
		yield();						// waiting for the next cycle (1ms)
	}	
}	