import os, ROOT, unrolling

dir = "./histograms/"

Histograms  = os.listdir(dir)
signals     = [s for s in Histograms if "T2tt" in s]
data        = [d for d in Histograms if "data" in d]
backgrounds = [b for b in Histograms if (b not in signals and b not in data)]

backgrounds_string = [b[:-5] for b in backgrounds] #remove .root

def main(WhatToDo, HistogramToUse):

    for signal in signals:

        if WhatToDo == "counting":
            makesimplecards([signal], HistogramToUse)
        elif WhatToDo == "1Dshape":
            makeshapecards1D([signal], HistogramToUse, "1Dshape")
        elif WhatToDo == "2Dshape":
            makeshapecards2D([signal], HistogramToUse, "2Dshape")
        elif WhatToDo == "3Dshape":
            makeshapecards3D([signal], HistogramToUse, "3Dshape")
        else:
            print '\n' + "Wrong input, didn't do anything." + '\n' + '\n'
            main()

def makesimplecards(signal, HistogramToUse):
    signal_string = [s[:-5] for s in signal] #remove .root

    allsystematics = simplesystematic(signal)
    extra = ''
    for i in range(len(signal)+len(backgrounds)): 
        extra +='{'+str(i)+':^19} '
    ones                        = extra.format(*([1]*(len(signal)+len(backgrounds))))
    stringSignalAndBackgrounds  = extra.format(*(signal_string+backgrounds_string))
    processline                 = extra.format(*range(len(backgrounds)+1))
    rates                       = extra.format(*getsimplerates(signal, HistogramToUse))
    #start writing
    output = open('./DATACARDS_counting/simple-counting-experiment_'+signal_string[0]+'.txt', 'w')
    output.write("# Simple counting experiment, with one signal and a few background processes" +'\n' + '\n' \
                     "imax  1  number of channels" + '\n' \
                     "jmax  " +str(len(backgrounds))+"  number of backgrounds" + '\n' \
                     "kmax  " +str(len(allsystematics))+"  number of nuisance parameters (sources of systematic uncertainties)" + '\n' \
                     "--------------------" + '\n' \
                     "#counting experiment->integral->single bin" + '\n' \
                     "bin           1" + '\n' \
                     "observation   "+str(getsimpledatarate(HistogramToUse)) + '\n' + '\n' \
                     "--------------------" + '\n' \
                     "bin        " + ones  + '\n' \
                     "process    " + stringSignalAndBackgrounds+ '\n' \
                     "process    " + processline + '\n' \
                     "rate       " + rates + '\n' + '\n' \
                     "--------------------" + '\n' \
                     )
    for i in allsystematics: output.write(i + '\n')

def makeshapecards1D(signal, HistogramToUse, WhatToDo):
    signal_string = [s[:-5] for s in signal] #remove .root

    rootfile = writetree(signal, HistogramToUse, WhatToDo)
    shaperates = getshaperates(rootfile)

    allsystematics = shapesystematic()
    extra = ''
    for i in range(2): 
        extra +='{'+str(i)+':^19} '
    ones                        = extra.format(*[1,1])
    stringSignalAndBackground   = extra.format(*["signal","background"])
    processline                 = extra.format(*[0,1])
    rates                       = extra.format(*shaperates[:-1])
    #start writing
    output = open('./DATACARDS_1Dshape/simple-shapes-TH1_'+signal_string[0]+'.txt', 'w')
    output.write("imax  1  number of channels" + '\n' \
                     "jmax  1  number of backgrounds" + '\n' \
                     "kmax  *  number of nuisance parameters (sources of systematical uncertainties)" + '\n' \
                     "--------------------" + '\n' \
                     "shapes * * " + rootfile.replace("./DATACARDS_1Dshape/","") + " $PROCESS $PROCESS_$SYSTEMATIC" + '\n' \
                     "--------------------" + '\n' \
                     "bin           1" + '\n' \
                     "observation   " + str(shaperates[-1]) + '\n' + '\n' \
                     "--------------------" + '\n' \
                     "bin        " + ones  + '\n' \
                     "process    " + stringSignalAndBackground+ '\n' \
                     "process    " + processline + '\n' \
                     "rate       " + rates + '\n' + '\n' \
                     "--------------------" + '\n' \
                     )
    
    for i in allsystematics: output.write(i + '\n')


def makeshapecards2D(signal, HistogramToUse, WhatToDo):
    signal_string = [s[:-5] for s in signal] #remove .root

    rootfile = writetree(signal, HistogramToUse, WhatToDo)
    shaperates = getshaperates(rootfile)

    allsystematics = shapesystematic()
    extra = ''
    for i in range(2): 
        extra +='{'+str(i)+':^19} '
    ones                        = extra.format(*[1,1])
    stringSignalAndBackground   = extra.format(*["signal","background"])
    processline                 = extra.format(*[0,1])
    rates                       = extra.format(*shaperates[:-1])
    #start writing
    output = open('./DATACARDS_2Dshape/simple-shapes-TH2_'+signal_string[0]+'.txt', 'w')
    output.write("imax  1  number of channels" + '\n' \
                     "jmax  1  number of backgrounds" + '\n' \
                     "kmax  *  number of nuisance parameters (sources of systematical uncertainties)" + '\n' \
                     "--------------------" + '\n' \
                     "shapes * * " + rootfile.replace("./DATACARDS_2Dshape/","") + " $PROCESS $PROCESS_$SYSTEMATIC" + '\n' \
                     "--------------------" + '\n' \
                     "bin           1" + '\n' \
                     "observation   " + str(shaperates[-1]) + '\n' + '\n' \
                     "--------------------" + '\n' \
                     "bin        " + ones  + '\n' \
                     "process    " + stringSignalAndBackground+ '\n' \
                     "process    " + processline + '\n' \
                     "rate       " + rates + '\n' + '\n' \
                     "--------------------" + '\n' \
                     )
    
    for i in allsystematics: output.write(i + '\n')


def makeshapecards3D(signal, HistogramToUse, WhatToDo):
    signal_string = [s[:-5] for s in signal] #remove .root

    rootfile = writetree(signal, HistogramToUse, WhatToDo)
    shaperates = getshaperates(rootfile)

    allsystematics = shapesystematic()
    extra = ''
    for i in range(2): 
        extra +='{'+str(i)+':^19} '
    ones                        = extra.format(*[1,1])
    stringSignalAndBackground   = extra.format(*["signal","background"])
    processline                 = extra.format(*[0,1])
    rates                       = extra.format(*shaperates[:-1])
    #start writing
    output = open('./DATACARDS_3Dshape/simple-shapes-TH3_'+signal_string[0]+'.txt', 'w')
    output.write("imax  1  number of channels" + '\n' \
                     "jmax  1  number of backgrounds" + '\n' \
                     "kmax  *  number of nuisance parameters (sources of systematical uncertainties)" + '\n' \
                     "--------------------" + '\n' \
                     "shapes * * " + rootfile.replace("./DATACARDS_3Dshape/","") + " $PROCESS $PROCESS_$SYSTEMATIC" + '\n' \
                     "--------------------" + '\n' \
                     "bin           1" + '\n' \
                     "observation   " + str(shaperates[-1]) + '\n' + '\n' \
                     "--------------------" + '\n' \
                     "bin        " + ones  + '\n' \
                     "process    " + stringSignalAndBackground+ '\n' \
                     "process    " + processline + '\n' \
                     "rate       " + rates + '\n' + '\n' \
                     "--------------------" + '\n' \
                     )
    
    for i in allsystematics: output.write(i + '\n')


def writetree(signal, HistogramToUse, WhatToDo):
    signal_string = [s[:-5] for s in signal] #remove .root

    vechisto = []

    #SIGNAL
    f1 = ROOT.TFile.Open(dir+signal[0],"read")
    sig = f1.Get(HistogramToUse)
    sig.SetDirectory(0)
    if WhatToDo=="2Dshape": sig = unrolling.TwoD(sig)
    if WhatToDo=="3Dshape": sig = unrolling.ThreeD(sig)
    sig.SetName("signal")
    #sig.Scale(10./sig.Integral())
    vechisto.append(sig)

    #UNCERTAINTY SIGNAL
    sig_Up = StatUpOrDown(sig,"Up")
    sig_Up.SetDirectory(0)
    sig_Up.SetName("signal_sigmaUp")
    sig_Down = StatUpOrDown(sig,"Down")
    sig_Down.SetDirectory(0)
    sig_Down.SetName("signal_sigmaDown")
    
    vechisto.append(sig_Up)
    vechisto.append(sig_Down)

    #BACKGROUNDS
    for i,b in enumerate(backgrounds):
        f2 = ROOT.TFile.Open(dir+b,"read")
        t = f2.Get(HistogramToUse)
        t.SetDirectory(0)
        if WhatToDo=="1Dshape":
            if i == 0:
                backg = t
                backg.SetName("background")
            else:
                backg.Add(t)
        if WhatToDo=="2Dshape":
            t2D = unrolling.TwoD(t)
            t2D.SetDirectory(0)
            if i == 0:
                backg = t2D
                backg.SetName("background")
            else:
                backg.Add(t2D)
        if WhatToDo=="3Dshape":
            t3D = unrolling.ThreeD(t)
            t3D.SetDirectory(0)
            if i == 0:
                backg = t3D
                backg.SetName("background")
            else:
                backg.Add(t3D)

    #backg.Scale(10./backg.Integral())
    vechisto.append(backg)

    #UNCERTAINTY BACKGROUNDS
    backg_Up = StatUpOrDown(backg,"Up")
    backg_Up.SetDirectory(0)
    backg_Up.SetName("background_alphaUp")
    backg_Down = StatUpOrDown(backg,"Down")
    backg_Down.SetDirectory(0)
    backg_Down.SetName("background_alphaDown")

    vechisto.append(backg_Up)
    vechisto.append(backg_Down)

    #DATA
    f3 = ROOT.TFile.Open(dir+data[0],"read")
    dat = f3.Get(HistogramToUse)
    dat.SetDirectory(0)
    if WhatToDo=="2Dshape": dat = unrolling.TwoD(dat)
    if WhatToDo=="3Dshape": dat = unrolling.ThreeD(dat)
    dat.SetName("data_obs")
    vechisto.append(dat)

    #WRITING
    if WhatToDo=="1Dshape":   output = ROOT.TFile("./DATACARDS_"+WhatToDo+"/simple-shapes-TH1_"+signal_string[0]+".root","recreate")
    elif WhatToDo=="2Dshape": output = ROOT.TFile("./DATACARDS_"+WhatToDo+"/simple-shapes-TH2_"+signal_string[0]+".root","recreate")
    elif WhatToDo=="3Dshape": output = ROOT.TFile("./DATACARDS_"+WhatToDo+"/simple-shapes-TH3_"+signal_string[0]+".root","recreate")
    for i in vechisto:
        i.Write()
    output.Close()
    return output.GetName()

def getsimplerates(signal, HistogramToUse):
    rates = []
    for hist in signal+backgrounds:
        f = ROOT.TFile.Open(dir+hist,"read")
        treehist = f.Get(HistogramToUse)
        integral = treehist.Integral()
        rates.append(integral)
    return rates

def getsimpledatarate(HistogramToUse):
    f = ROOT.TFile.Open(dir+data[0],"read")
    treehist = f.Get(HistogramToUse)
    integral = treehist.Integral()
    return integral

def getshaperates(rootfile):
    rates = []
    f = ROOT.TFile.Open(rootfile,"read")
    rates.append(f.Get("signal").Integral())
    rates.append(f.Get("background").Integral())
    rates.append(f.Get("data_obs").Integral())
    return rates

def simplesystematic(signal):
    listofsyst = [] 
    syst = {\
        'lumi':   {'label':'lnN','string':"   " },
        'bkg':    {'label':'lnN','string':"   " },
        'signal': {'label':'lnN','string':"   " },
        }
    
    for s in signal+backgrounds:
        syst['lumi']['string']+="1.12   "
        if s in backgrounds: 
            syst['bkg']['string']+="1.3  "
            syst['signal']['string']+="-   "
        else:
            syst['bkg']['string']+= "-   "
            syst['signal']['string']+="1.2   "
    for key in syst.keys():
        listofsyst.append(key+"\t"+syst[key]['label']+"\t"+syst[key]['string'])
    return listofsyst

def shapesystematic():
    listofsyst = [] 
    syst = {\
        'lumi':   {'label':'lnN','string':"   " },
        'alpha':  {'label':'shapeN2','string': "   "},
        'sigma':  {'label':'shapeN2','string': "   "},
        }
    
    syst['lumi']['string']+="1.12   1.12"
    syst['alpha']['string']+="-     1"
    syst['sigma']['string']+="1     -"

    for key in syst.keys():
        listofsyst.append(key+"\t"+syst[key]['label']+"\t"+syst[key]['string'])
    return listofsyst

def StatUpOrDown(hist, UpOrDown):
    histclone = hist.Clone()
    if UpOrDown == "Up": 
        #for bin in range(hist.GetNbinsX()): histclone.SetBinContent(bin+1, hist.GetBinContent(bin+1) + hist.GetBinError(bin+1))
        for bin in range(hist.GetNbinsX()): histclone.SetBinContent(bin+1, hist.GetBinContent(bin+1)*1.3)
    elif UpOrDown == "Down": 
        #for bin in range(hist.GetNbinsX()): histclone.SetBinContent(bin+1, hist.GetBinContent(bin+1) - hist.GetBinError(bin+1))
        for bin in range(hist.GetNbinsX()): histclone.SetBinContent(bin+1, hist.GetBinContent(bin+1)*0.7)
    else: print "Didn't use function properly"
    return histclone


if __name__ == "__main__":
    main()
