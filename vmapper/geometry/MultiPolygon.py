# -*- coding: utf-8 -*-

from ._common_util import getsty, getanim, render

class MultiPolygon:
    def __init__(self, exterior, index=0, layer='', label='', interiors=[], color=None, opacity=None, strokecolor=None, strokewidth=None, showlabel=False, animate_times=None, visibility='visible'):
        self.exterior = exterior
        self.interiors = interiors

        self.opacity = opacity
        self.strokewidth = strokewidth
        self.color = color
        self.strokecolor = strokecolor
        self.visibility = visibility
        self.animate_times = animate_times
        if not(label is None):
            self.label = label
        else:
            self.label = index
        self.idd = index
        self.tem_dict = dict(layername=layer,showlabel=showlabel,label=self.label,idd=index)
        self.tem = 'MultiPolygon.svg'

    def feature_string(self):
        mainstr = ''
        for polygon,inrings in zip(self.exterior, self.interiors):
            subfeature = get_pathstring(polygon)
            mainstr = mainstr + subfeature
            for inring in inrings:
                sub_in = get_pathstring(inring)
                mainstr = mainstr + sub_in
        sty = getsty(color=self.color, opacity=self.opacity, 
            strokecolor=self.strokecolor, strokewidth=self.strokewidth, 
            visibility=self.visibility)
        anim = getanim(self.idd, self.animate_times)
        self.tem_dict.update(dict(geom_str=mainstr, style_str=sty, anim_str=anim))
        string_done = render(self.tem, self.tem_dict)
        return string_done

def get_pathstring(vertexlist):
    if len(vertexlist)>1:
        string = 'M '
        for x, y in vertexlist:
            string = string + "{:.6f},{:.6f} L ".format(x, y)
            #"%.6f"%(x)+","+"%.6f"%(y)+" L "
        string = string[:-2]+'Z '
        return string
    else:
        print('vertexlist is too short (<2), returning None')
        return None
