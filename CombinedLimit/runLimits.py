import makeCards, os, ROOT, glob

def main():
    
    methods = {\
        "counting": {"folder":"./DATACARDS_counting/", "rootfiles":{}}, 
        "shape":    {"folder":"./DATACARDS_shape/", "rootfiles":{}},
        }

    for key in methods.keys():
        for f in glob.glob(methods[key]["folder"]+"*"): os.remove(f)
        print "Making the datacards, deleting all the old ones!" + '\n'
        makeCards.main(key)
        print "Datacards constructed" + '\n'
        os.chdir(methods[key]["folder"])
        
        datacards = os.listdir("./")
        datacards = [d for d in datacards if ".txt" in d]
        for datacard in datacards:
            print "Running combine function over datacard: ", datacard, '\n', '\n'
            os.system('combine -M Asymptotic '+datacard+ ' -n -'+datacard[:-4])
            print '\n', '\n'
        rootfiles = os.listdir("./")
        rootfiles = [r for r in rootfiles if "higgsCombine" in r]
        for rootfile in rootfiles: methods[key]["rootfiles"][rootfile] = {}
        os.chdir("../")

    print "Getting the r-values, will be stored in rValues.txt" + '\n'

    for key in methods.keys():
        for rootkey in methods[key]["rootfiles"].keys():
            f = ROOT.TFile.Open(methods[key]["folder"]+rootkey,"read")
            limit = f.Get("limit")
 
            limit.Draw("limit>>limit1", "quantileExpected==-1")
            limit1 = ROOT.gDirectory.Get("limit1")
            methods[key]["rootfiles"][rootkey]["limit1"] = limit1.GetMean()
            
            limit.Draw("limit>>limit2", "quantileExpected>0.02 && quantileExpected<0.03")
            limit2 = ROOT.gDirectory.Get("limit2")
            methods[key]["rootfiles"][rootkey]["limit2"] = limit2.GetMean()
            
            limit.Draw("limit>>limit16", "quantileExpected>0.15 && quantileExpected<0.16")
            limit16 = ROOT.gDirectory.Get("limit16")
            methods[key]["rootfiles"][rootkey]["limit16"] = limit16.GetMean()
            
            limit.Draw("limit>>limit50", "quantileExpected==0.5")
            limit50 = ROOT.gDirectory.Get("limit50")
            methods[key]["rootfiles"][rootkey]["limit50"] = limit50.GetMean()
            
            limit.Draw("limit>>limit84", "quantileExpected>0.83 && quantileExpected<0.94")
            limit84 = ROOT.gDirectory.Get("limit84")
            methods[key]["rootfiles"][rootkey]["limit84"] = limit84.GetMean()
            
            limit.Draw("limit>>limit97", "quantileExpected>0.97 && quantileExpected<0.98")
            limit97 = ROOT.gDirectory.Get("limit97")
            methods[key]["rootfiles"][rootkey]["limit97"] = limit97.GetMean()

    output = open('rValues.txt','w')
    extra = ''
    for i in range(len(methods["shape"]["rootfiles"].keys())+1): 
        extra +='{'+str(i)+':^31} '
    firstline = ['r-value']
    for rootfile in methods["shape"]["rootfiles"].keys(): 
        rootfile.replace("higgsCombine-simple-shapes-TH1_","")
        rootfile.replace(".Asymptotic.mH120.root", "")
        firstline.append(rootfile)
    output.write(extra.format(*firstline) + '\n')
    for key in methods.keys():
        line = []
        line.append(key)
        for rootfile in methods[key]["rootfiles"].keys():
            line.append(methods[key]["rootfiles"][rootfile]["limit50"])
        output.write(extra.format(*line)+'\n')

if __name__ == "__main__":
    main()
