import os, time
dirtocheck = os.getcwd()    
with open(dirtocheck+ "/automatedhist.txt","w") as f:    
    for file in os.listdir(dirtocheck):        
        if file.endswith("pptx"):
            thefile = dirtocheck+"//"+file
            f.writelines(f"\t{file :<30}{time.ctime(os.path.getmtime(thefile)) : >30}")            
            f.writelines("\n")