# Copyright (C) 2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import tokenresponse as token


def getUrl():
    return "/v1/faqgen"


def getReqData():
    # return {
    #     "inputs": "What is the revenue of Nike in last 10 years before 2023? Give me detail",
    #     "parameters": {"max_new_tokens": 128, "do_sample": True},
    # }
    # return {"query": "What is the revenue of Nike in last 10 years before 2023? Give me detail", "max_tokens": 128}
    return {"messages": "What is the revenue of Nike in last 10 years before 2023? Give me detail", "max_tokens": 128}


def respStatics(environment, reqData, respData):
    return token.respStatics(environment, reqData, respData)


def staticsOutput(environment, reqlist):
    token.staticsOutput(environment, reqlist)
