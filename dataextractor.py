{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3066368-ca0f-412a-a167-5da914ba101f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import re\n",
    "\n",
    "def process_data(dd_file='January_2017_Record_Layout.txt', data_file='dec17pub.dat', output_file='finaldata3.csv'):\n",
    "    dd_dic = open(dd_file, 'r', encoding='iso-8859-1').read()\n",
    "\n",
    "    series = ['HRYEAR4', 'HRMONTH', 'HRHHID', 'HUFINAL', 'HEHOUSUT', 'HRHTYPE', 'HETELHHD', 'HETELAVL', 'HEPHONEO', 'HUINTTYP', 'HEFAMINC', 'GEDIV', 'PTDTRACE']\n",
    "\n",
    "    r = re.compile('\\n(\\w+)\\s+(\\d+)\\s+(.*?)\\t+.*?(\\d\\d*).*?(\\d\\d+)')\n",
    "\n",
    "    dd_var = [(i[0], int(i[3])-1, int(i[4]))\n",
    "              for i in r.findall(dd_dic) if i[0] in series]\n",
    "\n",
    "    usdata = [tuple(int(line[i[1]:i[2]]) for i in dd_var)\n",
    "               for line in open(data_file, 'rb')]\n",
    "\n",
    "    dff = pd.DataFrame(usdata, columns=[v[0] for v in dd_var])\n",
    "\n",
    "    dff.to_csv(output_file, index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
