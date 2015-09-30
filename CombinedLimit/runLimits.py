import makeCards, os, ROOT, glob

def main():
    
    #directory where your histrograms are stored
    directory = "./histograms_ward_10fb_met40_metsig0_njets2ormore_bnjets1ormore_dphi0.25/"
    
    #mt2llcut for the CNC
    mt2llcut = 150

    lumi = 10 #in fb-1

    print '\n', '\n', "Running over " + str(lumi) + " fb histograms!", '\n', '\n'

    sigunc = 0.2 #20% uncertainty on signal

    bkgunc = 0.25


    whathistogram   = "h1_mt2llcounting_mt2llcut_"+str(mt2llcut)
    #whathistogram   = "h1_mt2llcounting"+str(mt2llcut)
    what1Dhistogram = "h1_mt2ll"
    what2Dhistogram = "h2_mt2blblvsmt2ll"
    what3Dhistogram = "h3_mt2bbvsmt2blblvsmt2ll"


    methods = {\
        "0_counting (mt2ll>"+str(mt2llcut)+" GeV)": {"folder":"./DATACARDS_counting/", "rootfiles":{}}, 
        "1_1Dshape (mt2ll)":                        {"folder":"./DATACARDS_1Dshape/",  "rootfiles":{}},
        "2_2Dshape (mt2ll, mt2blbl)":               {"folder":"./DATACARDS_2Dshape/",  "rootfiles":{}},
        "3_3Dshape (mt2ll, mt2blbl, mt2bb)":        {"folder":"./DATACARDS_3Dshape/",  "rootfiles":{}},
        }

    for key in methods.keys():
        for f in glob.glob(methods[key]["folder"]+"*"): os.remove(f)
        print "Making the datacards, deleting all the old ones!" + '\n'
        if (key=="0_counting (mt2ll>"+str(mt2llcut)+" GeV)" ):   makeCards.main(key, whathistogram,lumi,directory,sigunc,bkgunc)
        elif (key=="1_1Dshape (mt2ll)"):   makeCards.main(key, what1Dhistogram,lumi,directory,sigunc,bkgunc)
        elif (key=="2_2Dshape (mt2ll, mt2blbl)"):   makeCards.main(key, what2Dhistogram,lumi,directory,sigunc,bkgunc)
        elif (key=="3_3Dshape (mt2ll, mt2blbl, mt2bb)"):   makeCards.main(key, what3Dhistogram,lumi,directory,sigunc,bkgunc)
        print "Datacards constructed" + '\n'
        # os.chdir(methods[key]["folder"])
        
        # datacards = os.listdir("./")
        # datacards = [d for d in datacards if ".txt" in d]
        # for datacard in datacards:
        #     print "Running combine function over datacard: ", datacard, '\n', '\n'
        #     os.system('combine -M Asymptotic '+datacard+ ' -n -'+datacard[:-4]+" --run blind")
        #     print '\n', '\n'
        # rootfiles = os.listdir("./")
        # rootfiles = [r for r in rootfiles if "higgsCombine" in r]
        # for rootfile in rootfiles: methods[key]["rootfiles"][rootfile] = {}
        # os.chdir("../")

    # print "Getting the r-values, will be stored in rValues.txt" + '\n'

    # for key in methods.keys():
    #     for rootkey in methods[key]["rootfiles"].keys():
    #         f = ROOT.TFile.Open(methods[key]["folder"]+rootkey,"read")
    #         limit = f.Get("limit")
 
    #         limit.Draw("limit>>limit1", "quantileExpected==-1")
    #         limit1 = ROOT.gDirectory.Get("limit1")
    #         methods[key]["rootfiles"][rootkey]["limit1"] = round(limit1.GetMean(),4)
            
    #         limit.Draw("limit>>limit2", "quantileExpected>0.02 && quantileExpected<0.03")
    #         limit2 = ROOT.gDirectory.Get("limit2")
    #         methods[key]["rootfiles"][rootkey]["limit2"] = round(limit2.GetMean(),4)
            
    #         limit.Draw("limit>>limit16", "quantileExpected>0.15 && quantileExpected<0.16")
    #         limit16 = ROOT.gDirectory.Get("limit16")
    #         methods[key]["rootfiles"][rootkey]["limit16"] = round(limit16.GetMean(),4)
            
    #         limit.Draw("limit>>limit50", "quantileExpected==0.5")
    #         limit50 = ROOT.gDirectory.Get("limit50")
    #         methods[key]["rootfiles"][rootkey]["limit50"] = round(limit50.GetMean(),4)
            
    #         limit.Draw("limit>>limit84", "quantileExpected>0.83 && quantileExpected<0.94")
    #         limit84 = ROOT.gDirectory.Get("limit84")
    #         methods[key]["rootfiles"][rootkey]["limit84"] = round(limit84.GetMean(),4)
            
    #         limit.Draw("limit>>limit97", "quantileExpected>0.97 && quantileExpected<0.98")
    #         limit97 = ROOT.gDirectory.Get("limit97")
    #         methods[key]["rootfiles"][rootkey]["limit97"] = round(limit97.GetMean(),4)

    # output = open('rValues.txt','w')

    # output.write("[Lumi = "+str(lumi)+" fb{-1}]" + "\n" + '\n')

    # extra = ''
    # for i in range(len(methods["0_counting (mt2ll>"+str(mt2llcut)+" GeV)"]["rootfiles"].keys())+1): 
    #     extra +='{'+str(i)+':^35} '
    # firstline = ['Expected r-value']
    # for rootfile in sorted(methods["0_counting (mt2ll>"+str(mt2llcut)+" GeV)"]["rootfiles"].keys()): 
    #     rootfile = rootfile.replace("higgsCombine-simple-counting-experiment_","")
    #     rootfile = rootfile.replace(".Asymptotic.mH120.root", "")
    #     firstline.append(rootfile)
    # output.write(extra.format(*firstline) + '\n')
    # output.write("*"*(len(methods["0_counting (mt2ll>"+str(mt2llcut)+" GeV)"]["rootfiles"].keys())+1)*35 + '\n')
    # for key in sorted(methods.keys()):
    #     line = []
    #     line.append(key[2:])
    #     for rootfile in sorted(methods[key]["rootfiles"].keys()):
    #         #line.append(str(methods[key]["rootfiles"][rootfile]["limit2"]) + " - " + str(methods[key]["rootfiles"][rootfile]["limit50"]) + " - " + str(methods[key]["rootfiles"][rootfile]["limit97"]))
    #         line.append(str(methods[key]["rootfiles"][rootfile]["limit50"]))
    #     output.write(extra.format(*line)+'\n')

if __name__ == "__main__":
    main()
