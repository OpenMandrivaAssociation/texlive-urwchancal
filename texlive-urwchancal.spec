%global tl_name urwchancal
%global tl_revision 21701

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Use URWs clone of Zapf Chancery as a maths alphabet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/urwchancal
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/urwchancal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/urwchancal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows (the URW clone of) Zapf Chancery to function as a
maths alphabet, the target of \mathcal or \mathscr, with accents
appearing where they should, and other spacing parameters set to
reasonable (not very tight) values. The font itself may be found in the
URW basic fonts collection. This package supersedes the pzccal package.

