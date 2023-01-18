%======================================================================
% Indian Institue of Technology Bombay, Thesis Document Class for LaTeX2e
% This document class loads report class
% v1.0 Feb 2016	- First version
% v1.1 Feb 2019 - First version modified
% It is a class file: chthes.cls
% Use it as \documentclass[options]{chthes}
% Copyright (C) 2016 C. Has
% chthes.cls time stamp: 17:10, 10 Feb 2016 ; Chandra Has
% chthes.cls v1.1 time stamp: 12:10, 10 Feb 2019 ; Chandra Has
%
% Author electronic mail: chandrahashbti@gmail.com
%**********************************************************************

% IMPORTANT POINTS:

%********************************************************************
% This class can also be used without the thesis template
% It works with LaTeX, PDFLaTeX, XeLaTeX and LuaLaTeX
% Report to author if you find some errors in this file
% You are allowed to distribute this copy in any form without author  
% permission
% You can cange the name of the class file
% Your suggestions will be highly appreciated
%====================================================================

%********************* New class: chthes.cls*************************
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{settings/chthes}[2019/02/10 v1.1 A typographic style for nice-looking thesis]
\typeout{Document Class 'chthes' v1.1 < 10 Feb 19>}


%*******************************************************************
% Class version 
%******************************************************************
\def\chthesversion#1{\gdef\@chthesversion{#1}}
\def\@chthesversion{\textit{Version:} v1.1 2019/02/10}


%************Options of class***************************************
% Warning message for worng option
% Paper size
% Page type: twoside, oneside
% Font size
%*******************************************************************
\DeclareOption{a4paper}{%
	\setlength{\paperheight}{297mm}%
	 \setlength{\paperwidth}{210mm}%
	  }

\DeclareOption{a5paper}
{\ClassError{option}{Sorry, you are not allowed to use 'a5paper' in this class}{}
}

\DeclareOption{openbib}{\OptionNotUsed}
\DeclareOption{8pt}{\ClassWarning{chthesis}{Option '8pt' is not applicable}}

\newif\if@oneside\@onesidefalse
\newif\if@openany\@openanyfalse
\DeclareOption{oneside}{\PassOptionsToClass{\CurrentOption}{report}\@onesidetrue}%
\DeclareOption{twoside}{\PassOptionsToClass{\CurrentOption}{report}}%
\DeclareOption{openany}{\PassOptionsToClass{\CurrentOption}{report}\@openanytrue}%
\DeclareOption{openright}{\PassOptionsToClass{\CurrentOption}{report}}%

\def\@@ptsize{12pt} % default size
\DeclareOption{10pt}{\def\@@ptsize{10pt}}
\DeclareOption{11pt}{\def\@@ptsize{11pt}}
\DeclareOption{12pt}{\def\@@ptsize{12pt}}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\DeclareOption*{\PassOptionsToPackage{\CurrentOption}{report}}

%******************************************************************** 
% We need options to switch between dissertation, annual progress 
% seminar report, and thesis, and between different types of  
% reports. 
%*******************************************************************
\newif\if@aps
\newif\if@thesis
\newif\if@dissertation
\newif\if@project
\DeclareOption{aps}{\@apstrue}
\DeclareOption{thesis}{\@thesistrue}
\DeclareOption{dissertation}{\@dissertationtrue}
\DeclareOption{project}{\@projecttrue}

%*****************************************************************
% Process given options
% Defaults
%****************************************************************** 
\ProcessOptions\relax
\LoadClass[\@@ptsize, a4paper]{report}


%****************Some important packages***************************
% nag: for notification if any old command is used
% ams: for maths
% xcolor: for accessing color
% setspace: line spacing
% footmisc: footmark at bottom (should be uploaded before fancyhdr)
% fancyhdr: fancy headr and footer
% geometry: for page margins
% ifthen: conditional purpose
% emptypage: removes fancy headr-footer from the blank page
% nomencl: list of symbols
% natbib: to create references
% tocbibind: adds lof, lot, and ref. into toc
%********************************************************************
%\RequirePackage[l2tabu, orthodox]{nag}
\RequirePackage{amsmath,amsfonts,amssymb}
\RequirePackage{xcolor}
\RequirePackage{setspace}     
\RequirePackage[bottom]{footmisc} 
\RequirePackage{fancyhdr}\pagestyle{fancy}
\RequirePackage{ifthen}
\RequirePackage[intoc,refpage]{nomencl}\makenomenclature
\RequirePackage[round, sort & compress]{natbib}
\RequirePackage{geometry}
\RequirePackage[nottoc]{tocbibind}


%******************header-footer from fancyhdr.sty******************
\fancyhf{} % remove the old format
\if@twoside
\fancyhead[LO]{\em\nouppercase\rightmark} % for section
\fancyhead[RE]{\em\nouppercase\leftmark } % for chapter
\else
\fancyhead[L]{\em\nouppercase\rightmark}
\fi
\fancyhead[LE,RO]{\em\bfseries\thepage}
\cfoot{}
\renewcommand{\headrulewidth}{1pt}
%\renewcommand{\footrulewidth}{1pt}

\fancypagestyle{plain}{%                   % custom plain style
	\fancyhf{} 
	\cfoot{{\em\bfseries\thepage}}
	\renewcommand{\headrulewidth}{0pt}
	\renewcommand{\footrulewidth}{0pt}
}

% Heading style
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection~#1}}
\fancyheadoffset{0cm} % adjust the headrule offset

% Removes the header from odd empty pages  
\renewcommand*{\cleardoublepage}{%
 \clearpage\if@twoside\ifodd\value{page}\else
  \mbox{}%
   \thispagestyle{empty}{%
% 	\null\vfill
%   	\color{gray!70!black}\hspace*{\fill} 
%   	\textit{This page intentionally left blank}
%   	 \hspace*{\fill}\vfill\null
  }
\newpage%
\if@twocolumn\mbox{}\newpage
\fi\fi\fi
}


%****************************page margins*****************************
% Adjusted to a4paper (297 x 210 mm)
%\if@twoside 
% \geometry{left=3.5cm, right=2.5cm,	top=3.2cm, bottom=3.5cm}
% \else 
% \geometry{left=3cm, right=3cm,	top=3.2cm, bottom=3.5cm}
% \fi 	   
%  \setlength{\headheight}{1cm} 	 
%   \setlength{\footskip}{1.3cm}  
          
\setlength{\hoffset}{-1in} % already accounted for in the margins
\setlength{\voffset}{-1in} % already accounted for in the margins

\setlength{\topmargin}{15mm}
\setlength{\textheight}{245mm}
%\setlength\footskip{13mm}
\setlength{\headheight}{10mm}
\setlength{\headsep}{5mm}
% bottom margin is 22mm

\setlength{\textwidth}{150mm}
\if@twoside
\setlength{\oddsidemargin}{34mm} 
\setlength{\evensidemargin}{26mm}
\else
\setlength{\oddsidemargin}{30mm}  
\setlength{\evensidemargin}{30mm} 
\fi
% total width for two side: 160+30+20=210 mm


%******************notations with nomecl***************************
\renewcommand*{\pagedeclaration}[1]{~\dotfill\hyperpage{#1}}
\renewcommand*{\nompreamble}{\@mkboth{\nomname}{\nomname}}

\renewcommand*{\nomgroup}[1]{%
\ifthenelse{\equal{#1}{A}}{\item[\large \textbf{Roman Symbols}]}{%               
 \ifthenelse{\equal{#1}{B}}{\vskip5mm\item[\large\textbf{Greek Symbols}]}{%          
 \ifthenelse{\equal{#1}{C}}{\vskip5mm\item[\large\textbf{Superscripts}]}{%
 \ifthenelse{\equal{#1}{D}}{\vskip5mm\item[\large\textbf{Subscripts}]}{%	     
 \ifthenelse{\equal{#1}{E}}{\vskip5mm\item[\large\textbf{Acronyms}]}{% 
 \ifthenelse{\equal{#1}{X}}{\vskip5mm\item[\large\textbf{\@OtherSym}]}{%           
  }}}}}}
}

\newcommand*{\nmR}[3][]{\nomenclature[A#1]{#2}{#3}}
\newcommand*{\nmG}[3][]{\nomenclature[B#1]{#2}{#3}}
\newcommand*{\nmS}[3][]{\nomenclature[C#1]{#2}{#3}}
\newcommand*{\nms}[3][]{\nomenclature[D#1]{#2}{#3}}
\newcommand*{\nmA}[3][]{\nomenclature[E#1]{#2}{#3}}

\def\OtherSym#1{\gdef\@OtherSym{#1}}
\def\@OtherSym{Other Symbols}
\newcommand*{\nmX}[3][]{\nomenclature[X#1]{#2}{#3}}

\newcommand*{\nm}[2]{\nomenclature{#1}{#2}} % for simple list

%\newcommand*{\Unit}[1]{%
%	\renewcommand{\nomentryend}{%
%		\hspace*{\hfill}[#1]\nolinebreak\hspace*{4cm}\mbox{}}%
	
%\newcommand*{\nomheaders}{%
%	\item[\bfseries Symbol]%
%	\textbf{Description}\hfill\textbf{Page}\ignorespaces
%	}	


%******************reference and citation styles**********************
\renewcommand*{\bibname}{References}
%\let\chcite\cite
%\renewcommand{\cite}[1]{\textbf{\chcite{#1}}}
%\let\chcitet\citet
%\renewcommand{\citet}[1]{\textbf{\chcitet{#1}}}
%\let\chcitep\citep
%\renewcommand{\citep}[1]{\textbf{\chcitep{#1}}}
%\bibpunct{\color{blue}{(}}{\color{blue})}{;}{}{,}{,} 

%****************** Document body**************************************
% Three main parts: front-, main-, and backmatter.
% Defines the page number styles
% Option for including in toc
% Page styles
%**********************************************************************
\newcommand*{\frontmatter}{%
	\onehalfspacing\listpage\pagenumbering{roman}
	}
\newcommand*{\mainmatter}{%
	\cleardoublepage\onehalfspacing\pagestyle{fancy}\pagenumbering{arabic}%
	\setcounter{page}{1}
	}
\newcommand*{\backmatter}{%
	\cleardoublepage\onehalfspacing\pagestyle{fancy}
	}
\newcommand*{\addintoc}[1]{%
	\addcontentsline{toc}{chapter}{#1}
	}


%**********************Title page*************************************
% \author, \title are already defined in report
% Some new commands are defined here
% New commands: department, submissiondate, degreetype, supervisor,
% university, rollnum, logo
% A new command for accessing various fonts
% Use other font if the used font is not installed in your system
% Comments are welcomed
%**********************************************************************
\def\deptartment#1{\gdef\@deptartment{#1}}
\def\submitiondate#1{\gdef\@submitiondate{#1}}
\def\degreetype#1{\gdef\@degreetype{#1}}
\def\supervisor#1{\gdef\@supervisor{#1}}
\def\cosupervisor#1{\gdef\@cosupervisor{#1}}
\def\university#1{\gdef\@university{#1}}
\def\rollnum#1{\gdef\@rollnum{#1}}
\def\reporttype#1{\gdef\@reporttype{#1}}
\def\logo#1{\gdef\@logo{#1}}
\global\let\@cosupervisor\@empty
\global\let\@rollnum\@empty


\def\@logo{\color{black}\rule{3cm}{3cm}} % default logo
\def\@degreetype{Doctor of Philosophy}   % default degreetype
\def\@reporttype{A Project Report}

\nonstopmode          % Do not stop if the font is not available 
\newcommand*{\chfont}[1]{\fontfamily{#1}\selectfont} % Font 
\newfont{\degfont}{eufb10 scaled\magstep2} 
\newfont{\titlefont}{cmssdc10 scaled\magstep4}
%\errorstopmode       % revert back to stop on error

\def\@medskip{0.12in}
\def\@bigskip{0.47in}
\def\@biggskip{0.55in}
% Title page
\def\maketitle{%	 
\begin{titlepage}
\setcounter{page}{0} 
\addtocounter{page}{-1}   % For a page that should not be counted
\thispdfpagelabel{Title}
{\renewcommand{\baselinestretch}{1}\normalsize	 
	\begin{center}
	{		  	  
 	   {\bfseries\Large \@title\par}
 	   \vspace{\stretch{0.35}}	
			
		\large \if@aps Annual Progress Seminar Report \else \if@thesis  A Thesis \fi \if@dissertation A Dissertation \fi \if@project  \@reporttype  \fi \fi \par \vspace{\stretch{0.3}}
			
		Submitted in partial fulfillment of the requirements  \\[.25\baselineskip] 				
		for the degree of \par \vspace{\stretch{0.3}}	
		{\large \if@dissertation Master of Technology \else \if@thesis    \@degreetype \fi \if@aps \@degreetype \fi \if@project  \@degreetype \fi \fi } \\ [.25\baselineskip] 				
		{\large by \par} \vspace{.25\baselineskip} 		
		{\large \bfseries \@author\par}
		
		\ifx\@rollnum\@empty
		 \vspace{\stretch{0.3}}
		 \else 
		\vspace{.25\baselineskip}  
		{\large (Roll no.~\@rollnum)}
		\fi
				
		\vspace{\stretch{0.3}}				
		\ifx\@cosupervisor\@empty
		{\large  Supervisor:\par}\vspace{.25\baselineskip}  
		{\large \bfseries \@supervisor \par}
		\else 
		{\large Supervisors:\par} \vspace{.25\baselineskip}  
		{\large \bfseries  \@supervisor \par} \vspace{.25\baselineskip}    
		and \par \vspace{.25\baselineskip}      
		{\large\bfseries \@cosupervisor \par}
		\fi           
		\vspace{\stretch{0.3}}				
	
		\@logo \par \vspace{\stretch{0.3}}	                           
		{\large \@deptartment \par}
		\vspace{.25\baselineskip} 	
	    {\large \@university \par}\vspace{\stretch{0.3}}	
	   \vspace{\stretch{0.3}}
	   			
		{\large\bfseries \@submitiondate}	
	}	
	\end{center}
 }
%	\@chthesversion	
\end{titlepage}
\thispdfpagelabel{-} %for back side of cover page
}


%**************************Copyright page******************************
\newcommand*{\mycopyright}{%
	\cleardoublepage 	
	\thispagestyle{empty} 
	\setcounter{page}{0} 
	 \addtocounter{page}{-1}
	 \thispdfpagelabel{Copyright}
{	\setlength{\parindent}{0pt}	 
	\vspace*{19cm} 
\itshape\copyright\,\footnotesize \@submitiondate, by \@author\\	
All rights reserved}
\clearpage\thispdfpagelabel{-}
}


%**************************Dedication ********************************
\newcommand*{\dedication}[1][]{%
\cleardoublepage
\thispagestyle{empty} 
\setcounter{page}{0} 
\addtocounter{page}{-1}
\thispdfpagelabel{Dedication}
{\centering\large\itshape\null\vfill #1\vfill\null}
\clearpage\thispdfpagelabel{-}
  }

%**************************Approval sheet*****************************
\newcommand{\makeapproval}[1][Approval Sheet]{%
 \cleardoublepage	
  \thispagestyle{empty}
  \setcounter{page}{0} 
  \addtocounter{page}{-1}
  \thispdfpagelabel{Approval}
  \begin{center}
    {\LARGE \bfseries #1}\\[1\baselineskip]
    \normalsize
   \end{center}
    \normalsize This \if@dissertation  dissertation \else \if@thesis  doctoral thesis \fi \if@aps  doctoral thesis \fi \if@project  \@reporttype\ \fi \fi entitled ``\@title'' by \@author\ is approved for the degree of  \if@dissertation Master of Technology \else \if@thesis \@degreetype \fi \if@aps \@degreetype \fi \if@project  \@degreetype \fi \fi .
 \begin{center}
 \vspace*{10mm}
 \renewcommand{\arraystretch}{2} 	
 		\begin{tabular}{p{0.45\linewidth}c}
 			& \rule{6.5cm}{1pt}\\
 			& \rule{6.5cm}{1pt} \\
 			& \rule{6.5cm}{1pt} \\[-7mm]
 			& {Examiners} \\[7mm]
 			& \rule{6.5cm}{1pt} \\
 			& \rule{6.5cm}{1pt} \\
 			& \rule{6.5cm}{1pt} \\[-7mm]
 			& Supervisor (s) \\[7mm]
 			& \rule{6.5cm}{1pt}\\[-7mm]
 			& Chairman \\
 			Date: \rule{3cm}{1pt} & \\
 			Place: \rule{3cm}{1pt} &\\			
 		\end{tabular}   	
 		\end{center} 
  \clearpage\thispdfpagelabel{-}
 }	  


%**************************Declaration********************************
\newcommand*{\DecSign}[1][\today]{% 
	\vspace{3cm}  
	\begin{center}	
		\begin{tabular}{p{0.67\linewidth}c}
			& \rule{4cm}{1pt}\\			
			& \@author\\[-2mm]
			\ifx\@rollnum\@empty
							Date: #1 & \\
							\else 	
			& (\@rollnum) \\[1cm]
			Date: #1 & \\
			\fi	          
		\end{tabular}	
	\end{center}
}

\newenvironment{Declaration}[1][Declaration]{%
 \cleardoublepage
 \pagestyle{plain}		
\setcounter{page}{1}
 \chapter*{#1}
}{}


%*************************Certificate***********************************
\newcommand*{\makecertificate}[1][Certificate]{%
	\cleardoublepage	
	\thispagestyle{plain}
		\begin{center}	
			{\Large \textbf{#1} }\leavevmode\\[1cm]
			{\large\textbf{\@deptartment}}\leavevmode\\
			{\large\textbf{\@university}}
		\end{center}\leavevmode\\[1cm] 
		\noindent
		\if@aps Annual progress seminar report \else \if@thesis The Thesis \fi \if@dissertation A dissertation \fi \if@project  \@reporttype \fi \fi	 entitled ``\@title'' submitted by \@author~%
		\ifx\@rollnum\@empty						
		 may be accepted for being evaluated.\leavevmode\\[2cm]
		\noindent
		Date: \hfill (\@supervisor) 
		\else
		(Roll no.~\@rollnum) may be accepted for being evaluated.\leavevmode\\[2cm]
				\noindent
				Date: \hfill (\@supervisor) 
 }
 
 
%*************************Acknowledgements******************************
\newenvironment{Acknowledgements}[1][Acknowledgements]{%
\cleardoublepage
\chapter*{#1}}{%
\@mkboth{Acknowledgements}{Acknowledgements}
}

\newenvironment{Plainacknowledgements}[1][Acknowledgements]{%
\cleardoublepage
\chapter*{#1}}{\pagestyle{plain}
 }

\newcommand*{\signature}[2][IIT Bombay]{%
	\vspace{1cm}
		\begin{flushright}
			\emph{\bfseries \@author}\\
			#1 \\ #2
		\end{flushright}
	}


%*************************Abstract**************************************
\newenvironment{Abstract}[1][Abstract]{%
\cleardoublepage
\chapter*{#1}}{%
\@mkboth{Abstract}{Abstract}
 }


%*************************Makecontents**********************************
% Change contents name
% Adding lof and lot into toc
% Adding toc into pdf bookmark
%***********************************************************************
\renewcommand*{\contentsname}{Table of Contents}
\newenvironment{contentlist}{%
\cleardoublepage
}{}
\newcommand*{\tocrule}{%
\addtocontents{toc}{\protect\addvspace{20pt}\hrule\protect\addvspace{10pt}}
}

\newcommand*{\listpage}{\addtocontents{toc}{%	
{\bfseries\color{blue!80!black}\textit{Contents}\hfill\textit{Page}}\par}
	}

\let\mytoc\tableofcontents
\renewcommand{\tableofcontents}{%
	\pdfbookmark[0]{\contentsname}{toc}	
	\mytoc
	\@mkboth{\contentsname}{\contentsname}
	}

\let\mylof\listoffigures
\renewcommand{\listoffigures}{%	
	\mylof%
	\@mkboth{\listfigurename}{\listfigurename}	
}

\let\mylot\listoftables
\renewcommand{\listoftables}{%
	\mylot%
	\@mkboth{\listtablename}{\listtablename}	
}

%*************************Symbol list*********************************
\newcommand*{\notations}[2][4cm]{%
	\cleardoublepage
	\pagestyle{fancy}
	\renewcommand*{\nomname}{#2}%		
	\printnomenclature[#1]	
	}


%*************************Appendix************************************
\RequirePackage[toc,page]{appendix}
%\RequirePackage{etoolbox} 
%\newcommand*{\appendixpagenumbering}{%
%	\pretocmd{\chapter}{%
%		\cleardoublepage	
%		\pagenumbering{Roman}%
%		\setcounter{page}{1}
%		\renewcommand*{\thepage}{\thechapter.~\Roman{page}}%
%	}{}{}	
%}
%\newcommand*{\Appendix}[1][]{%
%	\cleardoublepage\appendix #1}


%**********************List of publication****************************
\newcommand*{\pubpagenum}{%
	\pagenumbering{Roman}\setcounter{page}{1}
	\renewcommand*{\thepage}{P.~\Roman{page}}
		}
\newenvironment{Publications}[1][List of Publications]{%
\cleardoublepage 
\chapter*{#1}
\addintoc{List of Publications}}{%
\@mkboth{List of Publications}{List of Publications}
}


%***********************Footnote and float setting*******************
% Space between last line of text and footnote rule
% Very untidy way to get it!
% Redefine the macro used for footnotes to use single spacing
% This part is taken from MIT (many thanks to them)
%*******************************************************************
\skip\footins 20pt plus 4pt minus 4pt 

\long\def\@footnotetext#1{\insert\footins{\def\baselinestretch{1}\footnotesize
		\interlinepenalty\interfootnotelinepenalty 
		\splittopskip\footnotesep
		\splitmaxdepth \dp\strutbox \floatingpenalty \@MM
		\hsize\columnwidth \@parboxrestore
		\edef\@currentlabel{\csname p@footnote\endcsname\@thefnmark}\@makefntext
		{\rule{\z@}{\footnotesep}\ignorespaces
			#1\strut}}}


%*******************************************************************
% Fix up spacing before and after displayed math
% (arraystretch seems to do a fine job for inside LaTeX displayed math,
% since array and eqnarray seem to be affected as expected)
%*******************************************************************
\everydisplay{
	\abovedisplayskip \baselinestretch\abovedisplayskip%
	\belowdisplayskip \abovedisplayskip%
	\abovedisplayshortskip \baselinestretch\abovedisplayshortskip%
	\belowdisplayshortskip  \baselinestretch\belowdisplayshortskip}


%********************* Paragraph, line spacing********************
% Indentation 5 characters approx
% Paragraph spacing
% Line spacing (onehalfspacing is equal to baselinestretch 1.33)
%*****************************************************************
\parindent 5ex
%\setlength{\parskip}{1\baselineskip} 
%\renewcommand{\baselinestretch}{1.33}


%**************************Other settings****************************
% Indentation setting, line stretch and float setup
% Widow and orphan settings
%*******************************************************************
%	\brokenpenalty=10000
	\clubpenalty=10000   % To remove orphan (single line at bottom of page)
	\widowpenalty=10000	 % and widow (single line at top of page)
	 	

%\renewcommand{\textfraction}{0.4}
%\setlength{\textfloatsep}{40pt plus 2pt minus 1pt}
%\renewcommand{\topfraction}{1}
%\renewcommand{\bottomfraction}{0.65}
%\renewcommand{\textfraction}{0}
%\setcounter{topnumber}{2}
%\setcounter{bottomnumber}{2}
%\setcounter{totalnumber}{4}


%*********Chapter, section, subsection, subsubsection spacing*********
% chapter style is taken from report.cls
% \@startsection{name}{level}{indent}{beforeskip}{afterskip}{style}
%********************************************************************
\def\@makechapterhead#1{%
	\vspace*{50\p@}%
	{\parindent \z@ \centering \normalfont
		\ifnum \c@secnumdepth >\m@ne
		\huge\bfseries \@chapapp\space \thechapter
		\par\nobreak
		\vskip 20\p@
		\fi
		\interlinepenalty\@M
		\Huge \bfseries #1\par\nobreak
		\vskip 40\p@
	}}
	
	\def\@makeschapterhead#1{%
		\vspace*{50\p@}%
		{\parindent \z@ \centering
			\normalfont
			\interlinepenalty\@M
			\Huge \bfseries  #1\par\nobreak
			\vskip 40\p@
		}}

%*************************Section/subsection/subsubsection*************
\renewcommand{\section}{\@startsection{section}{1}%
	\z@{-.7\baselineskip\@plus-\baselineskip}{.5\baselineskip}%
	{\large\normalfont\bfseries\hsize0.8\textwidth \raggedright}}

\renewcommand{\subsection}{\@startsection{subsection}{2}%
	\z@{.5\baselineskip\@plus.7\baselineskip}{0.5\baselineskip}%
	{\normalfont\bfseries\raggedright}}

\renewcommand{\subsubsection}{\@startsection{subsubsection}{3}{\z@}%
	{-3.25ex\@plus -1ex \@minus -.2ex}%
	{1.5ex \@plus .2ex}%
	{\normalfont\itshape\raggedright}}


%******************Some other packages*************************** 
% Hyperref, bookmark, and cleveref packages
% bookmar and cleveref should be uploaded after hyperref
%**************************************************************** 
\RequirePackage[pdfstartview=Fit, pdfusetitle]{hyperref}         
%
\RequirePackage{cleveref} 

\endinput

% File \textit{chthes.cls} ends here.
%===================================================================



















