require 'rubygems'
require 'mechanize'

UTCS_URL = 'http://www.cs.utexas.edu/~igtanase/'

agent = Mechanize.new

page = agent.get(UTCS_URL)

pp page
