<h1> Pre-Requsites </h1>
<ol>
  <li>PIP</li>
  <li>Python 3.7</li>
</ol>
 


<h1>Requirements Installation</h1>
Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)

<h1>Overview</h1>

<h2>Fix_Message_Generator.py</h2>
This script has one input will generate (number_of_messages_to_generate) which defines how many randomly generated fix messages will be created.
The fix messages follow a specific strucutre with the items in {} being the variables that will differ:
<br>8=FIX.4.2|35=D|55={symbol}|54={side}|38={quantity}|40={ordType}|59={timeInForce}|167={securityType}|1={account}|44={price}.</br>

The messages will be written to a text file in the current directory the script is being run from.
Running the script by calling the script name will generate 1000 messages by default.


<h2>Fix_Message_Statistics.py</h2>
This script will call Fix_Message_Reader to read the generated messages from the step above. It will then process the messages to supply some statistics about the messages.
The statistics will be printed in the console.

Statistics available:
- List Of All Products Traded
- Most Popular Order
- Stats About OrdType
- Stats About Quantity
- Stats About Price
- Average Quantity per OrdType
- Average Price Per OrdType
