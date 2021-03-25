import sys
import re
import fileinput

# def replace(name):
#     with open(name) as fp:
#         line = fp.readline()
#         while line:
#             if "\[caption id=" in line:
#                 print("{}".format(line.strip()))
#             line = fp.readline()


# \[caption id="attachment\_80" align="alignnone" width="300" caption="F/6.3・1/640sec・ISO200"\][![](https://blog.naotaco.com/assets/images/posts/2010/07/DSC00175-300x199.jpg "SONY DSC")](https://blog.naotaco.com/assets/images/posts/2010/07/DSC00175.jpg)\[/caption\] 

def main(argv):
    for line in fileinput.input(inplace=True):
        if "\[caption" in line:
            # print(line.replace("\[caption",""),end='') # this goes to the current file
            new_line = re.sub(re.escape("\[caption id")+".*\!","| !",line)
            caption = re.sub(".*\)","",new_line)
            new_line = re.sub("\).*",") |",new_line)
            print(new_line,end='')
            print("|:--:|")
            caption2 = caption.replace("\[/caption\]","").rstrip()
            print('| %s |' % caption2)
        else:
            print(line,end='')

if __name__ == "__main__":
    main(sys.argv)
