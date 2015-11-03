import ROOT, os
import numpy as n

#directory where your histrograms are stored
directory = "./histograms_ward_10fb_met140_metsig8_njets2ormore_bnjets1ormore_dphi0.25_DY_HT/"
#directory = "./histograms_ward_10fb_met140_metsig8_njets2ormore_bnjets1ormore_dphi0.25bin111/"
#directory = "./histograms_ward_10fb_met140_metsig8_njets2ormore_bnjets1ormore_dphi0.25/"
#directory = "./histograms_ward_10fb_met80_metsig5_njets2ormore_bnjets1ormore_dphi0.25/"
#directory = "./histograms_ward_10fb_met40_metsig0_njets2ormore_bnjets1ormore_dphi0.25/"

HistogramToUse = "h3_mt2bbvsmt2blblvsmt2ll"

def main():
    
    dir = directory

    Histograms  = os.listdir(dir)
    signals     = [s for s in Histograms if "T2tt" in s]
    data        = [d for d in Histograms if "data" in d]
    backgrounds = [b for b in Histograms if (b not in signals and b not in data)]
    
    backgrounds_string = [b[:-5] for b in backgrounds] #remove .root

    table = {}

    for b in backgrounds+signals:

        table[b] = {}
        table['totalbkg'] = {}

        fileth3 = ROOT.TFile.Open(dir+b,"read")
        th3 = fileth3.Get(HistogramToUse)
        th3.SetDirectory(0)

        nbinsX = th3.GetNbinsX()
        nbinsY = th3.GetNbinsY()
        nbinsZ = th3.GetNbinsZ()

        mt2llrange = []
        for i in range(nbinsX+1):
            mt2llrange.append(int(th3.GetXaxis().GetBinLowEdge(i+1)))
        mt2blblrange = []
        for i in range(nbinsY+1):
            mt2blblrange.append(int(th3.GetYaxis().GetBinLowEdge(i+1)))
        mt2bbrange = []
        for i in range(nbinsZ+1):
            mt2bbrange.append(int(th3.GetZaxis().GetBinLowEdge(i+1)))

        for i in range(1,nbinsX+1):
            table[b][i]={}
            for j in range(1,nbinsY+1):
                table[b][i][j]={}
                for k in range(1,nbinsX+1):
                    number = th3.GetBinContent(i,j,k)
                    error  = th3.GetBinError(i,j,k)
                    table[b][i][j][k] = [number,error]

    for i in range(1,nbinsX+1):
        table['totalbkg'][i]={}
        for j in range(1,nbinsY+1):
            table['totalbkg'][i][j]={}
            for k in range(1,nbinsX+1):
                totalbkg =   sum([table[b][i][j][k][0] for b in backgrounds])
                totalerror = sum([table[b][i][j][k][1] for b in backgrounds])
                table['totalbkg'][i][j][k] = [totalbkg,totalerror]

    totalbkg_allbins = 0.
    totalbkgerror_allbins = 0.
    for i in range(1,nbinsX+1):
        for j in range(1,nbinsY+1):
            for k in range(1,nbinsZ+1):
                totalbkg_allbins += table['totalbkg'][i][j][k][0]
                totalbkgerror_allbins += table['totalbkg'][i][j][k][1]
                
    if totalbkg_allbins > 10: 
        totalbkg_allbins = int(totalbkg_allbins)
        totalbkgerror_allbins = round(totalbkgerror_allbins,1)
    elif totalbkg_allbins > 1: 
        totalbkg_allbins = round(totalbkg_allbins,1)
        totalbkgerror_allbins = round(totalbkgerror_allbins,1)
    else: 
        totalbkg_allbins = round(totalbkg_allbins,3)
        totalbkgerror_allbins = round(totalbkgerror_allbins,3)

    totalsignal_allbins = [0.]*len(signals)
    totalsignalerror_allbins = [0.]*len(signals)
    for l,s in enumerate(sorted(signals)):
        fileth3 = ROOT.TFile.Open(dir+s,"read")
        th3 = fileth3.Get(HistogramToUse)
        th3.SetDirectory(0)
        a = n.zeros(1, dtype=float)
        totalsignal_allbins[l] = th3.IntegralAndError(1,nbinsX,1,nbinsY,1,nbinsZ,a)
        totalsignalerror_allbins[l] = a[0]
        if totalsignal_allbins[l]>100:
            totalsignal_allbins[l] = int(totalsignal_allbins[l])
            totalsignalerror_allbins[l] = round(totalsignalerror_allbins[l],1)
        elif totalsignal_allbins[l]>10:
            totalsignal_allbins[l] = round(totalsignal_allbins[l],1)
            totalsignalerror_allbins[l] = round(totalsignalerror_allbins[l],1)
        else:
            totalsignal_allbins[l] = round(totalsignal_allbins[l],3)
            totalsignalerror_allbins[l] = round(totalsignalerror_allbins[l],3)

    for i in range(1,nbinsX+1):
        for j in range(1,nbinsY+1):
            for k in range(1,nbinsZ+1):
                if table['totalbkg'][i][j][k][0] > 10:    table['totalbkg'][i][j][k] = [int(table['totalbkg'][i][j][k][0]),round(table['totalbkg'][i][j][k][1],1)]
                elif table['totalbkg'][i][j][k][0] > 1:   table['totalbkg'][i][j][k] = [round(table['totalbkg'][i][j][k][0],1),round(table['totalbkg'][i][j][k][1],1)]
                else:                                     table['totalbkg'][i][j][k] = [round(table['totalbkg'][i][j][k][0],3),round(table['totalbkg'][i][j][k][1],3)]
                for s in signals+backgrounds:
                    if table[s][i][j][k][0] > 10:   table[s][i][j][k] = [int(table[s][i][j][k][0]),round(table[s][i][j][k][1],1)]
                    elif table[s][i][j][k][0] > 1:  table[s][i][j][k] = [round(table[s][i][j][k][0],1),round(table[s][i][j][k][1],1)]
                    else:                           table[s][i][j][k] = [round(table[s][i][j][k][0],3),round(table[s][i][j][k][1],3)]


    output = open("./3Dtable.tex","w")

    output.write("\\documentclass[8pt,landscape]{article}" + '\n')
    output.write("\\usepackage[margin=0.5in]{geometry}" + '\n')
    output.write("\\usepackage{verbatim}" + '\n')
    output.write("\\usepackage{hyperref}" + '\n')
    output.write("\\usepackage{epsfig}" + '\n')
    output.write("\\usepackage{graphicx}" + '\n')
    output.write("\\usepackage{epsfig}" + '\n')
    output.write("\\usepackage{subfigure,              rotating,              rotate}" + '\n')
    output.write("\\usepackage{relsize}" + '\n')
    output.write("\\usepackage{fancyheadings}" + '\n')
    output.write("\usepackage{multirow}" + '\n')
    output.write("\\usepackage[latin1]{inputenc}" + '\n')
    output.write("\\usepackage{footnpag}" + '\n')
    output.write("\\usepackage{enumerate}" + '\n')
    output.write("\\usepackage{color}" + '\n')
    output.write("\\newcommand{\\doglobally}[1]{{\\globaldefs=1#1}}" + '\n')
    output.write("\\begin{document}" + '\n' \
                     "\\begin{small}" + '\n')
    
  
    output.write("\\begin{tabular}{|c|c|c||c|c|c|c|c|c|}" + '\n')
    output.write("\\cline{6-9}" + '\n' )
    output.write("\\multicolumn{1}{c}{} &\\multicolumn{1}{c}{}&\\multicolumn{1}{c}{}&\\multicolumn{1}{c}{}&\\multicolumn{1}{c}{}& \\multicolumn{4}{|c|}{\\textcolor{red}{\\textbf{Signal Point Considered}}} \\\\ \\cline{4-9} \n")
    string = "\\multicolumn{1}{c}{}&\\multicolumn{1}{c}{} &\\multicolumn{1}{c|}{} & bin & bkg" 
    for s in sorted(signals): 
        st = filter(str.isdigit, s)[2:]
        st = "(" + st[:3] + "," + st[3:] + ")"
        string += "& " + st
    string += "\\\\ \\hline \\hline \n"
    output.write(string)
    l=0
    for i,ikey in enumerate(table['totalbkg'].keys()):
        for j,jkey in enumerate(table['totalbkg'][ikey]):
            for k,kkey in enumerate(table['totalbkg'][ikey][jkey]):
                l+=1
                if j==0:
                    if k==0:
                        string = "\\multirow{"+str(nbinsY*nbinsZ)+"}{*}{"+str(mt2llrange[i])+"$\leq$MT2ll$<$"+str(mt2llrange[i+1])+" GeV} & \\multirow{"+str(nbinsZ)+"}{*}{"+str(mt2blblrange[j])+"$\leq$MT2blbl$<$"+str(mt2blblrange[j+1])+" GeV} & "+str(mt2bbrange[k])+"$\leq$MT2bb$<$"+str(mt2bbrange[k+1])+" GeV & "+str(l) + "&" +str(table['totalbkg'][ikey][jkey][kkey][0])+"$\\pm$"+str(table['totalbkg'][ikey][jkey][kkey][1])
                        for s in sorted(signals): string += "& " +str(table[s][ikey][jkey][kkey][0])+"$\\pm$"+str(table[s][ikey][jkey][kkey][1])
                        string += "\\\\ \n"
                        output.write(string)
                    else:
                        string = " & & "+str(mt2bbrange[k])+"$\leq$MT2bb$<$"+str(mt2bbrange[k+1])+" GeV & "+str(l) + "&"+str(table['totalbkg'][ikey][jkey][kkey][0])+"$\\pm$"+str(table['totalbkg'][ikey][jkey][kkey][1])
                        for s in sorted(signals): string += "& " +str(table[s][ikey][jkey][kkey][0])+"$\\pm$"+str(table[s][ikey][jkey][kkey][1])
                        string += "\\\\ \n"
                        output.write(string)
                else: 
                    if k==0:
                        string = " & \\multirow{"+str(nbinsZ)+"}{*}{"+str(mt2blblrange[j])+"$\leq$MT2blbl$<$"+str(mt2blblrange[j+1])+" GeV} & "+str(mt2bbrange[k])+"$\leq$MT2bb$<$"+str(mt2bbrange[k+1])+" GeV & "+str(l) + "&"+str(table['totalbkg'][ikey][jkey][kkey][0])+"$\\pm$"+str(table['totalbkg'][ikey][jkey][kkey][1])
                        for s in sorted(signals): string += "& " +str(table[s][ikey][jkey][kkey][0])+"$\\pm$"+str(table[s][ikey][jkey][kkey][1])
                        string += "\\\\ \n"
                        output.write(string)
                    else:
                        string = " & & "+str(mt2bbrange[k])+"$\leq$MT2bb$<$"+str(mt2bbrange[k+1])+" GeV & "+str(l) + "&"+str(table['totalbkg'][ikey][jkey][kkey][0])+"$\\pm$"+str(table['totalbkg'][ikey][jkey][kkey][1])
                        for s in sorted(signals): string += "& " +str(table[s][ikey][jkey][kkey][0])+"$\\pm$"+str(table[s][ikey][jkey][kkey][1])
                        string += "\\\\ \n"
                        output.write(string)
                output.write("\\cline{3-9}" + '\n')
            output.write("\\cline{2-9}" + '\n')
        output.write("\\hline \\hline" + '\n')
    
    string = " \multicolumn{3}{|c||}{Total} & \multicolumn{1}{|c|}{} &" + str(totalbkg_allbins)+"$\\pm$"+str(totalbkgerror_allbins)
    for i in range(len(totalsignal_allbins)): string += " & " + str(totalsignal_allbins[i]) + "$\\pm$" + str(totalsignalerror_allbins[i])
    string += "\\\\ \\hline \n"

    output.write(string)
  
    output.write("\\end{tabular}" + '\n' \
                 "\\end{small}" + '\n')
    
    output.write("\\end{document}")


if __name__ == "__main__":
    main()
