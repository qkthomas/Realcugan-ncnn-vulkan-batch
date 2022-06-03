#!/usr/bin/env python3

#weight: #1 shortest, #2 smallest total scale factor

import sys

factorLst = [2, 3, 4]
sepStr = ":"
resMap = {}

def lstToStr(lst: list) -> str:
    strVal = sepStr.join([str(x) for x in lst])
    # print(strVal)
    return strVal

def strTolst(str: str) -> list:
    numLst = []
    strLst = str.split(sepStr)
    for str in strLst:
        numLst.append(int(str))
    return numLst

def calMagTotalFactor(seq: list) -> int:
    totalFactor = 1
    for factor in seq:
        totalFactor = totalFactor * factor
    return totalFactor

def calMagSeq(scale, resPrev: list):
    if scale <= 1:
        # no need to upscale. save the result
        resPrev.sort()
        global resMap
        resMap[lstToStr(resPrev)] = True
        return
    for factor in factorLst:
        cpyResPrev = []
        for ele in resPrev:
            cpyResPrev.append(ele)
        cpyResPrev.append(factor)
        calMagSeq(scale/factor, cpyResPrev)

def getBestSeq() -> list:
    bestSeqs = []
    global resMap
    for seqStr in resMap:
        lst = strTolst(seqStr)
        length = len(lst)
        if len(bestSeqs) == 0 or length == len(bestSeqs[0]):
            bestSeqs.append(lst)
            continue
        if length < len(bestSeqs[0]):
            bestSeqs = [lst]
            continue

    bestSeq = []
    for seq in bestSeqs:
        if len(bestSeq) == 0 or calMagTotalFactor(seq) < calMagTotalFactor(bestSeq):
            bestSeq = seq

    return bestSeq

def getScaleFromArgs():
    scaleStr = sys.argv[1]
    if "." in scaleStr:
        return float(scaleStr)
    return int(scaleStr)

emptyLst = []
scale = getScaleFromArgs()
calMagSeq(scale, emptyLst)
print(getBestSeq())