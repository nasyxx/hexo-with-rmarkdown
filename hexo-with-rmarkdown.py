import sys

#sys.argv[0]
file_Rhtml = sys.argv[1]

def checkback(string, pattern):
	if len(string) < len(pattern):
		return False
	elif pattern == string[len(string)-len(pattern):]:
		return True
	else:
		return False

class Rmd:
	def __init__(self, filename):
		f = open(filename, 'r')
		self.data = f.readlines()
		self.start = 0
		self.end = len(self.data) - 1
	def gotoline(self, pattern, key):
		data = self.data
		start = self.start
		end = self.end
		if key == 'forward':
			while not checkback(data[start].strip(), pattern):
				start += 1
			self.start = start
		elif key == 'backward':
			while not checkback(data[end].strip(), pattern):
				end -= 1
			self.end = end

def main():
	Rhtml = Rmd(file_Rhtml)
	Rhtml.gotoline('</title>', 'forward')
	start = Rhtml.start
	Rhtml.gotoline('</div>', 'backward')
	end = Rhtml.end
	#print Rhtml.data[start:end+1]
	#output
	f = open(file_Rhtml+".hexo.md", 'w+')
	f.write("{% raw %}\n"+"".join(Rhtml.data[start:end+1])+"{% endraw %}")

main()