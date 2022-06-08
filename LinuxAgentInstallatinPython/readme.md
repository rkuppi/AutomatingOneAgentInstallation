# Automating oneAgent Installation for Linux
## Pre-requisites to run the script on Windows
* Python should be installed (preferred version >=3.7)</br>
   Guide: https://www.python.org/</br>
   Paramiko, openpyxl and cryptography modules</br>
  * If required modules are not present, try installing them using pip</br>
    Help: https://docs.python.org/3/installing/index.html </br>
    Ex: python3 -m pip3 install [modulename]</br>
	  (or)</br>
  *	Run this command:</br?
  Requirement.txt file is in the folder.</br>
  <Folder location> py -m pip install -r requirements.txt</br>

  Help: https://packaging.python.org/tutorials/installing-packages/ </br>
  fine the requirements.txt in the directory</br>
* Open Required ports
* Oneagent binary

# Steps for the installation
1. Create the excel sheet using below templet and follow the same header naming conventions. This naming conventions are used in the script.</br>
  Reference Template.xlsx in Installation Direcitory</br>
  Follow dynatrace documentation for naming conventions:</br>
   https://www.dynatrace.com/support/help/setup-and-configuration/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux/ 
2. Please fill “- “, “none”, or leave the cell “blank” if you wish to avoid giving value to a parameter.
  [image](https://user-images.githubusercontent.com/95140620/172542279-0f5f25d9-3d13-408e-9332-100ed7af9133.png)
3. Save this file somewhere in the local disk.
4. Download the OneAgent binary file for Linux and place this binary in the same folder where the actual script is placed and rename it to “Dynatrace.sh” 
5. For installation and uninstallation first, we need to run the setup script (OneAgentInstallationSetupLinux.py, LinuxOneAgentUnstallationSetup.py)
6. This script will take absolute paths of the excel sheet as input and generate “encrypted file” and “unlock.key” file where the main main script and setup scripts are placed. </br>
  Give absolute path (fill path):</br>
  Make sure you are in correct directory link and run the following command:</br>
< OneAgentInstallationSetupLinux.py  location> python3 OneAgentInstallationSetupLinux.py </br>
  ![image](https://user-images.githubusercontent.com/95140620/172542543-a1fd2bc7-2709-4a5a-939e-211fa3ee4266.png)</br>
  If script is executed successfully then, there are files in the same folder where the script is placed. As follows</br>
 **Note**: If there is only one user credentials to log in to the server, you no need to fill the credentials in excel sheet, instead you can directly update it in the   script. Remove the highlighted data “please update here” and replace with user name and password </br>
  (eg: client.connect(host, 22, username = “someuser”, password = “password”) (line no:104 in main script)
6.	Run the main script</br>

  **Command**:</br>
  <Script location> python3 OneAgentInstallationLinux.py</br>
  Script will automatically create the log file if is not exist, append to the previous file if the log file already exists. Check log files for installation     details. (OneAgentInstallationLinux.py)</br>
  Script will create the “successfull_Installation_list.txt” file. If oneAgent services are running on the host then script will add servername/FQDN mentioned in the excel sheet to this file.</br>
  
  
  Script will create “unable_to_installList.txt” file, if there are any errors during execution. Server name will be added to this list as well as the reason for installation failures on specific server.</br>
  
  
  Output:</br>
  
  ![image](https://user-images.githubusercontent.com/95140620/172544558-a69911d4-c300-4835-902d-b7c6bd01dd49.png)

     
  If agent is installed successfully then we receive output as above templet. 
  We receive “OneAgent installation was successful on the –{host}” message for successful installation. </br>

  Look into logs for details on installation/Errors during installation
  






  
  
