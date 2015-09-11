import makeCards, os, ROOT, glob

def main():
    
    whathistogram = "h1_mT2LL"
    what2Dhistogram = "h2_test"
    what3Dhistogram = "h3_test"

    methods = {\
        "counting": {"folder":"./DATACARDS_counting/", "rootfiles":{}}, 
        "1Dshape":    {"folder":"./DATACARDS_1Dshape/",    "rootfiles":{}},
        #"2Dshape":  {"folder":"./DATACARDS_2Dshape/",  "rootfiles":{}},
        #"3Dshape":  {"folder":"./DATACARDS_3Dshape/",  "rootfiles":{}},
        }

    for key in methods.keys():
        for f in glob.glob(methods[key]["folder"]+"*"): os.remove(f)
        print "Making the datacards, deleting all the old ones!" + '\n'
        if (key=="counting" or key=="1Dshape"): makeCards.main(key, whathistogram)
        elif (key=="2Dshape"):                  makeCards.main(key, what2Dhistogram)
        elif (key=="3Dshape"):                  makeCards.main(key, what3Dhistogram)
        print "Datacards constructed" + '\n'
        os.chdir(methods[key]["folder"])
        
        datacards = os.listdir("./")
        datacards = [d for d in datacards if ".txt" in d]
        for datacard in datacards:
            print "Running combine function over datacard: ", datacard, '\n', '\n'
            os.system('combine -M Asymptotic '+datacard+ ' -n -'+datacard[:-4]+" --run blind")
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
            methods[key]["rootfiles"][rootkey]["limit1"] = round(limit1.GetMean(),4)
            
            limit.Draw("limit>>limit2", "quantileExpected>0.02 && quantileExpected<0.03")
            limit2 = ROOT.gDirectory.Get("limit2")
            methods[key]["rootfiles"][rootkey]["limit2"] = round(limit2.GetMean(),4)
            
            limit.Draw("limit>>limit16", "quantileExpected>0.15 && quantileExpected<0.16")
            limit16 = ROOT.gDirectory.Get("limit16")
            methods[key]["rootfiles"][rootkey]["limit16"] = round(limit16.GetMean(),4)
            
            limit.Draw("limit>>limit50", "quantileExpected==0.5")
            limit50 = ROOT.gDirectory.Get("limit50")
            methods[key]["rootfiles"][rootkey]["limit50"] = round(limit50.GetMean(),4)
            
            limit.Draw("limit>>limit84", "quantileExpected>0.83 && quantileExpected<0.94")
            limit84 = ROOT.gDirectory.Get("limit84")
            methods[key]["rootfiles"][rootkey]["limit84"] = round(limit84.GetMean(),4)
            
            limit.Draw("limit>>limit97", "quantileExpected>0.97 && quantileExpected<0.98")
            limit97 = ROOT.gDirectory.Get("limit97")
            methods[key]["rootfiles"][rootkey]["limit97"] = round(limit97.GetMean(),4)

    output = open('rValues.txt','w')
    extra = ''
    for i in range(len(methods["1Dshape"]["rootfiles"].keys())+1): 
        extra +='{'+str(i)+':^51} '
    firstline = ['Expected r-value']
    for rootfile in methods["1Dshape"]["rootfiles"].keys(): 
        rootfile = rootfile.replace("higgsCombine-simple-shapes-TH1_","")
        rootfile = rootfile.replace(".Asymptotic.mH120.root", "")
        firstline.append(rootfile)
    output.write(extra.format(*firstline) + '\n')
    for key in sorted(methods.keys()):
        line = []
        line.append(key)
        for rootfile in methods[key]["rootfiles"].keys():
            #line.append(str(methods[key]["rootfiles"][rootfile]["limit2"]) + " - " + str(methods[key]["rootfiles"][rootfile]["limit50"]) + " - " + str(methods[key]["rootfiles"][rootfile]["limit97"]))
            line.append(str(methods[key]["rootfiles"][rootfile]["limit50"]))
        output.write(extra.format(*line)+'\n')

if __name__ == "__main__":
    main()
