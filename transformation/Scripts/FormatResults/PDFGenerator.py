import os
import subprocess as sub
import shutil


def GetMainTex(title):
    #s = '\\documentclass{sig-alternate}\n'
    s = '\\documentclass{article}\n'

    s += '\\usepackage{multirow}\n'
    s += '\\usepackage{amsfonts}\n'
    s += '\\usepackage{epsfig}\n'
    s += '\\usepackage{amsmath}\n'
    s += '\\usepackage{amssymb}\n'
    s += '%\\usepackage[nolist]{acronym}\n'
    s += '\\usepackage[acronym]{glossaries}\n'
    s += '\\newcommand\\acro[2]{\\newacronym{#1}{#1}{#2}}\n'
    s += '\\newcommand\\acroAlwaysShort[1]{\\newglossaryentry{#1}{type=\\acronymtype, name={#1}, description={#1}, text={#1}, first={#1}, plural={#1s}, firstplural={#1s}}}\n'
    s += '\\newcommand\\ac[1]{\\gls{#1}}\n'
    s += '\\newcommand\\acp[1]{\\glspl{#1}}\n'
    s += '\\newcommand\\acs[1]{\\glsname{#1}}\n'
    s += '\\newcommand\\acl[1]{\\glsentrylong{#1}}\n'
    s += '\\usepackage[english]{babel}\n'
    s += '\\usepackage{cite}\n'
    s += '\\usepackage{color}\n'
    s += '\\usepackage[usenames,dvipsnames]{xcolor}\n'
    s += '%\\usepackage{stfloats}\n'
    s += '%\\usepackage{dblfloatfix}\n'
    s += '%\\usepackage{pst-gantt}\n'
    s += '% \\usepackage{algorithm}\n'
    s += '% \\usepackage{algorithmic}\n'
    s += '\\usepackage[linesnumbered,ruled,vlined,boxed,commentsnumbered]{algorithm2e}\n'
    s += '\\usepackage[noend]{algorithmic}\n'
    s += '\\usepackage{float}\n'
    s += '\\algsetup{linenosize=\\tiny}\n'
    s += '\\usepackage{caption}\n'
    s += '\\usepackage{subcaption}\n'
    s += '\\usepackage{pgfplots}\n'
    s += '\\usepackage{pgfplotstable}\n'
    s += '\\usepgfplotslibrary{statistics}\n'
    s += '\\pgfplotsset{compat=1.8} \n'
    s += '\\usepackage{booktabs}\n'
    s += '\\usepackage{listings}\n'
    s += '\\usepackage{todonotes}\n'
    s += '%\\usetikzlibrary{plotmarks}\n'
    s += '\\usetikzlibrary{shapes,positioning}\n'
    s += '\\usetikzlibrary{decorations,decorations.pathmorphing}\n'
    s += '\\usetikzlibrary{calc}\n'
    s += '\\usepackage{wrapfig}\n'
    s += '\\usepackage{enumitem}\n'
    s += '\\usepackage{url}\n'
    s += '\n'
    s += '\\usepackage[squaren,Gray]{SIunits}\n'
    s += '\\newcommand\\byte{B}\n'
    s += '\\newcommand\\bit{b}\n'
    s += '\\renewcommand\\per{p}\n'
    s += '\\renewcommand\\unit[2]{$#1$\\,#2}\n'
    s += '\\usepackage{tabularx}\n'
    s += '\n'
    s += '\\lstset{%\n'
    s += '  backgroundcolor=\\color{gray!25},\n'
    s += '  basicstyle=\\sffamily \\scriptsize,\n'
    s += '  breaklines=true\n'
    s += '}\n'
    s += '\n'
    s += '% fix the issue of white character in acronym package\n'
    s += '\\usepackage{etoolbox}\n'
    s += '\\makeatletter\n'
    s += '\\patchcmd\\@acf{\\hskip\\z@}{}{}{}\n'
    s += '\\patchcmd\\@acf{\\hskip\\z@}{}{}{}\n'
    s += '\\makeatother\n'
    s += '\n'
    s += '\\definecolor{gray11}{HTML}{000000}\n'
    s += '\\definecolor{gray12}{HTML}{777777}\n'
    s += '\\definecolor{gray13}{HTML}{aaaaaa}\n'
    s += '\\definecolor{gray14}{HTML}{cccccc}\n'
    s += '\n'
    s += '\n'
    s += '\\usepackage{pgfplotstable}\n'
    s += '\\pgfplotsset{compat=1.8}\n'
    s += '\n'
    s += '%\\pgfplotsset{compat=1.8}\n'
    s += '\n'
    s += '\\newcommand{\\parag}[1]{\\vspace{5pt}\\noindent\\textbf{#1}.\\quad}\n'
    s += '\\newcommand\\algoFontSize{8}\n'
    s += '\\newcommand{\\mat}{\\pmb}\n'
    s += '\\newcommand{\\TD}{T_{\\text{D}}}\n'
    s += '\\newcommand{\\TB}{T_{\\text{B}}}\n'
    s += '\\newcommand{\\Nf}{N_{\\text{f}}}\n'
    s += '\\newcommand{\\Dist}{ Dist }\n'
    s += '\\newcommand{\\virg}[1] {``{{#1}}''}\n'
    s += '\\newcommand{\\ist}[1]    {{#1}^{\\underline{\\text{st}}}}\n'
    s += '\\newcommand{\\latin}[1]{{\\it #1}}\n'
    s += '\\newcommand{\\red}[1] {\\textcolor[rgb]{1.0,0.0,0.0}{{#1}}}\n'
    s += '\\newcommand{\\blue}[1] {\\textcolor[rgb]{0.0,0.0,1.0}{{#1}}}\n'
    s += '\\newcommand{\\green}[1] {\\textcolor[rgb]{0.0,1.0,0.0}{{#1}}}\n'
    s += '\\newcommand\\newpara[1]{\\vspace{0.15cm}\\noindent\\textbf{#1}.\\hspace{0.15cm}}\n'
    s += '\n'
    s += '\\newcommand {\\otoprule }{\\midrule [\\heavyrulewidth]}\n'
    s += '\n'
    s += '\\title{'+title+'}\n'
    s += '\n'
    s += '\\tolerance=1\n'
    s += '\\emergencystretch=\\maxdimen\n'
    s += '\\hyphenpenalty=10000\n'
    s += '\\hbadness=10000\n'
    s += '\n'
    s += '\\floatstyle{ruled}\n'
    s += '\\newfloat{ilp}{ht}{aux}\n'
    s += '\\floatname{ilp}{Integer Linear Program}\n'
    s += '\n'
    s += '\n'
    s += '%\\numberofauthors{1}\n'
    s += '%\n'
    s += '%\\author{}\n'
    s += '\n'
    s += '\\begin{document}\n'
    s += '    \maketitle\n'
    #s += '{}\n'.format(title)
    s += '%\\begin{figure}\n'
    s += '%    \\input{box_plot.tex}\n'
    s += '%    \\caption{Box plot}\n'
    s += '%\\end{figure}\n'
    s += '\n'
    s += '\\begin{figure}\n'
    s += '    \\input{plot_distance.tex}\n'
    s += '    \\caption{Orthodromic distance to MS-SSIM}\n'
    s += '\\end{figure}\n'
    s += '\\begin{figure}\n'
    s += '    \\input{plot_distance_psnr.tex}\n'
    s += '    \\caption{Orthodromic distance to PSNR}\n'
    s += '\\end{figure}\n'
    for layoutId in ['cube', 'rhombic', 'pyramid', 'EquiTiled']:
        s += '\\begin{figure}\n'
        s += '    \\input{plot_distance_'+layoutId+'_psnr.tex}\n'
        s += '    \\caption{Orthodromic distance to PSNR for '+layoutId+'}\n'
        s += '\\end{figure}\n'
    s += '\\end{document}\n'
    return s

def GetBoxTex():
    s = '\\usetikzlibrary{pgfplots.statistics}\n'
    s += '\\newcommand\\storelabel[2]{\\expandafter\\xdef\\csname label#1\\endcsname{#2}}\n'
    s += '\\newcommand\\getlabel[1]{\\csname label#1\\endcsname}\n'
    s += '\n'
    s += '\\newcommand{\\newBoxplot}[5]{%\n'
    s += '    \\addplot+[ boxplot prepared={%\n'
    s += '            lower whisker={#1}, lower quartile={#2}, median={#3},\n'
    s += '            upper quartile={#4}, upper whisker={#5},% average={#6},\n'
    s += '    /pgf/number format/precision=2 } ]\n'
    s += '    coordinates {}\n'
    s += '    ;\n'
    s += '} %end of \\newBoxplot definition\n'
    s += '\n'
    s += '\\newcommand{\\newBoxPlotFromCdfFile}[2]{%\n'
    s += '    \\pgfplotstablegetelem{0}{#2}\\of{#1}\n'
    s += '    \\edef\\min{\\pgfplotsretval}\n'
    s += '    \\storelabel{min#1#2}{\\min}\n'
    s += '    \\pgfplotstablegetelem{50}{#2}\\of{#1}\n'
    s += '    \\edef\\qmin{\\pgfplotsretval}\n'
    s += '    \\storelabel{qmin#1#2}{\\qmin}\n'
    s += '    \\pgfplotstablegetelem{100}{#2}\\of{#1}\n'
    s += '    \\edef\\med{\\pgfplotsretval}\n'
    s += '    \\storelabel{med#1#2}{\\med}\n'
    s += '    \\pgfplotstablegetelem{150}{#2}\\of{#1}\n'
    s += '    \\edef\\qmax{\\pgfplotsretval}\n'
    s += '    \\storelabel{qmax#1#2}{\\qmax}\n'
    s += '    \\pgfplotstablegetelem{200}{#2}\\of{#1}\n'
    s += '    \\edef\\max{\\pgfplotsretval}\n'
    s += '    \\storelabel{max#1#2}{\\max}\n'
    s += '    \\newBoxplot{\\getlabel{min#1#2}}{\\getlabel{qmin#1#2}}{\\getlabel{med#1#2}}{\\getlabel{qmax#1#2}}{\\getlabel{max#1#2}}\n'
    s += '}\n'
    s += '\n'
    s += '\n'
    s += '\\pgfplotscreateplotcyclelist{My color list}{%\n'
    s += '    {black!50,solid,thick},%\n'
    s += '    {black!85,solid,thick}%\n'
    s += '}\n'
    s += '\n'
    s += '\\def\\ymin{0.7}\n'
    s += '\n'
    s += '\\begin{tikzpicture}\n'
    s += '    \\begin{axis}[\n'
    s += '            boxplot/draw direction=y,\n'
    s += '            ylabel={MS-SSIM},\n'
    s += '            width=1.05\\linewidth,\n'
    s += '            height=0.5\\linewidth,\n'
    s += '            boxplot={\n'
    s += '                draw position={1/3 + floor(0.01+\\plotnumofactualtype/2) + 1/3*mod(\\plotnumofactualtype,2)},\n'
    s += '                box extend=0.30,\n'
    s += '            },\n'
    s += '            %x=2cm,\n'
    s += '            xtick={0,1,2,...,10},\n'
    s += '            x tick label as interval,\n'
    s += '            xticklabels={%\n'
    s += '                {{\\tiny Good~Bad}},%\n'
    s += '                {{\\tiny Good~Bad}},%\n'
    s += '                {{\\tiny Good~Bad}},%\n'
    s += '                {{\\tiny Good~Bad}},%\n'
    s += '            },\n'
    s += '            x tick label style={\n'
    s += '                text width=2.5cm,\n'
    s += '                align=center\n'
    s += '            },\n'
    s += '            cycle list name={My color list},\n'
    s += '            legend cell align=left,\n'
    s += '            xmin = 0,\n'
    s += '            xmax = 4,\n'
    s += '            ymin = \\ymin,\n'
    s += '            ymax = 1,\n'
    s += '            axis on top,\n'
    s += '        ]\n'
    s += '        \\pgfplotsextra{\\begin{scope}[on layer=axis background]\n'
    s += '                \\draw[fill=gray!14,draw=gray!14] (axis cs:1,\\ymin) rectangle\n'
    s += '                (axis cs:2,1);\n'
    s += '                \\draw[fill=gray!14,draw=gray!14] (axis cs:3,\\ymin) rectangle\n'
    s += '                (axis cs:4,1);\n'
    s += '            \\end{scope}\n'
    s += '        }\n'
    s += '        \\newBoxPlotFromCdfFile{../cdfQuality.csv}{goodEquirectangularTiled}\n'
    s += '        \\newBoxPlotFromCdfFile{../cdfQuality.csv}{badEquirectangularTiled}\n'
    s += '\n'
    s += '        \\newBoxPlotFromCdfFile{../cdfQuality.csv}{goodCubeMap}\n'
    s += '        \\newBoxPlotFromCdfFile{../cdfQuality.csv}{badCubeMap}\n'
    s += '\n'
    s += '        \\newBoxPlotFromCdfFile{../cdfQuality.csv}{goodPyramidal}\n'
    s += '        \\newBoxPlotFromCdfFile{../cdfQuality.csv}{badPyramidal}\n'
    s += '\n'
    s += '        \\newBoxPlotFromCdfFile{../cdfQuality.csv}{goodRhombicDodeca}\n'
    s += '        \\newBoxPlotFromCdfFile{../cdfQuality.csv}{badRhombicDodeca}\n'
    s += '\n'
    s += '    \\end{axis}\n'
    s += '    \\begin{axis}[\n'
    s += '            width=1.05\\linewidth,\n'
    s += '            height=0.5\\linewidth,\n'
    s += '            xmin=0,xmax=4,\n'
    s += '            ymin=\\ymin,ymax = 1,\n'
    s += '            axis x line*=top,\n'
    s += '            axis y line=none,\n'
    s += '            enlargelimits=false,\n'
    s += '            hide y axis,\n'
    s += '            xtick={0,1,2,...,10},\n'
    s += '            x tick label as interval,\n'
    s += '            xticklabels={%\n'
    s += '                { EquiTiled },%\n'
    s += '                { Cube },%\n'
    s += '                { Pyramid },%\n'
    s += '                { Dodeca },%\n'
    s += '            },\n'
    s += '            x tick label style={\n'
    s += '                text width=2.5cm,\n'
    s += '                align=center\n'
    s += '            },\n'
    s += '        ]\n'
    s += '    \\end{axis}\n'
    s += '\n'
    s += '\\end{tikzpicture}\n'
    return s

def GetDistTex(plotPSNR, listId, filter=None):
    s = '\\pgfplotscreateplotcyclelist{My color list}{%\n'
    s += '    {gray,solid, very thick},%\n'
    s += '    {black!25, dashed, very thick},%\n'
    s += '    {black!75, densely dashed, very thick},%\n'
    s += '    {black, densely dotted, very thick},%\n'
    s += '}\n'
    s += '\n'
    s += '\\pgfplotsset{every axis legend/.append style={\n'
    s += '        at={(0,0.97)},\n'
    s += 'anchor=south west,\n'
    s += 'draw=none,\n'
    s += 'fill=none,\n'
    s += 'legend columns=1,\n'
    s += 'column sep=15pt,\n'
    s += '/tikz/every odd column/.append style={column sep=0cm},\n'
    s += '%font=\\tiny\n'
    s += '}}\n'
    s += '\\pgfplotsset{grid style={dashed,gray}}\n'
    s += '\\pgfplotsset{minor grid style={dotted,red!20!gray}}\n'
    s += '\\pgfplotsset{major grid style={dotted,green!50!black}}\n'
    s += '\n'
    s += '\n'
    s += '\\begin{tikzpicture}\n'
    s += '    \\begin{axis}[\n'
    s += '            ylabel={'+('PSNR' if plotPSNR else 'MS-SSIM')+'},\n'
    s += '            xlabel={Orthodromic distance},\n'
    s += '            width=1.05\\linewidth,\n'
    s += '            height=0.5\\linewidth,\n'
    s += ' %           unit vector ratio=1 2 1,\n'
    s += ' %           x=0.4cm,\n'
    s += '            cycle list name={My color list},\n'
    s += '            %ytick={0,2,4,...,10},\n'
    s += '            %xtick pos=left,\n'
    s += '            %x tick label style={at={(current axis.right of origin)},rotate=45,anchor=north east},\n'
    s += '            minor y tick num={4},\n'
    s += '            legend cell align=left,\n'
    s += '            xmin = 0,\n'
    s += '            xmax = 3.14,\n'
    s += '            %ymin = 0.7,\n'
    s += '            %ymax = 1,\n'
    s += '            ymajorgrids,\n'
    s += '            yminorgrids,\n'
    s += '%            axis on top,\n'
    s += '            %y filter/.code={\\pgfmathparse{#1/1000000}\\pgfmathresult},\n'
    s += '        ]\n'
    s += '\n'
    for layoutId in listId:
        if filter is None or filter in layoutId:
            s += '        \\addplot+ table [x=distance, y={}]{{../distanceQuality{}.csv}};\n'.format(layoutId, '_psnr' if plotPSNR else '')
    s += '        \\legend{'
    first = True
    for layoutId in listId:
        if filter is None or filter in layoutId:
            if first:
                first = False
            else:
                s+=', '
            s += layoutId
    s += '}\n'
    s += '\n'
    s += '    \\end{axis}\n'
    s += '\\end{tikzpicture}\n'
    return s

def GeneratePDF(pathToCsv, outputPath, title):
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)
    if not os.path.exists('{}/{}'.format(pathToCsv, 'cdfQuality.csv')) or not os.path.exists('{}/{}'.format(pathToCsv, 'distanceQuality.csv')) or not os.path.exists('{}/{}'.format(pathToCsv, 'distanceQuality_psnr.csv')):
        print ('Cannot generate the PDF because some csv files are missing')
        return

    with open('{}/main.tex'.format(outputPath), 'w') as main:
        main.write(GetMainTex(title))

    with open('{}/box_plot.tex'.format(outputPath), 'w') as box:
        box.write(GetBoxTex())

    listId = []
    with open('{}/{}'.format(pathToCsv, 'distanceQuality.csv'), 'r') as i:
        for line in i:
            if line[0] != '%':
                ids = line.split(' ')
                listId = ids[1:]
                break
    with open('{}/plot_distance.tex'.format(outputPath), 'w') as dist:
        dist.write(GetDistTex(False, listId))

    with open('{}/{}'.format(pathToCsv, 'distanceQuality_psnr.csv'), 'r') as i:
        for line in i:
            if line[0] != '%':
                ids = line.split(' ')
                listId = ids[1:]
                break

    with open('{}/plot_distance_psnr.tex'.format(outputPath), 'w') as dist:
        dist.write(GetDistTex(True, listId))

    with open('{}/plot_distance_cube_psnr.tex'.format(outputPath), 'w') as dist:
        dist.write(GetDistTex(True, listId, 'CubeMap'))

    with open('{}/plot_distance_rhombic_psnr.tex'.format(outputPath), 'w') as dist:
        dist.write(GetDistTex(True, listId, 'Rhombic'))

    with open('{}/plot_distance_pyramid_psnr.tex'.format(outputPath), 'w') as dist:
        dist.write(GetDistTex(True, listId, 'Pyramidal'))

    with open('{}/plot_distance_EquiTiled_psnr.tex'.format(outputPath), 'w') as dist:
        dist.write(GetDistTex(True, listId, 'EquirectangularTiled'))

    shutil.copyfile('../../academicPaper/sig-alternate.cls', '{}/sig-alternate.cls'.format(outputPath))
    sub.Popen([os.path.abspath('../../academicPaper/latexrun'), 'main.tex'], cwd=outputPath).wait()
