{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import necessary libraries\n",
    "from flask import Flask, render_template, jsonify, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create instance of Flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  create route that renders index.html template\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    return render_template(\"index.html\", mars=mars)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create a route that scrapes mars data\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "    mars = mongo.db.mars\n",
    "    mars_data = scrape_mars.scrape()\n",
    "    mars.update(\n",
    "        {},\n",
    "        mars_data,\n",
    "        upsert=True\n",
    "    )\n",
    "    return redirect(\"http://localhost:5000/\", code=302)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Python assigns \"__main__\" to the script  If the script is imported from another script, the script keeps it given name (e.g. hello.py). In our case we are executing the script. Therefore, __name__ will be equal to \"__main__\". That means the if conditional statement is satisfied and the app.run() method will be executed. This technique allows the programmer to have control over script’s behavior.\n",
    "#print any possible errors\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
