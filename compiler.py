import utils

sq = "6 + (-n * 2  + 4 - n) + (4n/4)3 + 6"
sq_1 = "(5.5)^n"

class sequenceCompiler(object):
    def __init__(self):
        self.data = {
            "stack":[]
        }
    def compiler(self,values,recurse=False):
        result = 0
        stack = self.data["stack"]

        if recurse:
            groups = utils.sorter([x["group"] for x in utils.calcPrecidence(values)],reverse=True,distinct=True)
            res = values
        else:
            groups = utils.sorter([x["group"] for x in utils.calcPrecidence(values[0])],reverse=True,distinct=True)
            res = values[0]
        
        if len(groups) == 0 and len(values) > 0:
            if type(values[0]) == list and len(values[0]) > 0:
                result = values[0][0]
            else:
                result = values[0]
        
        while len(groups) > 0:
            precidences = utils.calcPrecidence(res)
            index = 0
            temp_array = []
            skip = 0
            opcode_skip = 0
            for opcode in res:
                if utils.OPCODES.getOpcodes().__contains__(opcode):
                    if utils.getPrecidenceOpcode(opcode)["group"] == utils.getLastValue(groups):
                        pr = utils.getPrecidenceIndex(precidences,index)
                        match opcode:
                            case utils.OPCODES.EVAL:
                                execute = self.compiler(stack[utils.look_forward(res,pr["index"])],recurse=True)
                                temp_array.append(execute)
                                skip += 1
                            case _:
                                if len(temp_array) > 0:
                                    num_1 = utils.getLastValue(temp_array)
                                    num_2 = utils.look_forward(res,pr["index"])
                                    if num_2 == utils.OPCODES.SUB:
                                        num_2 = utils.execute(0,num_2,utils.look_forward(res,pr["index"]+1))
                                        opcode_skip += 1
                                    temp_array.pop()
                                    temp_array.append(utils.execute(num_1,opcode,num_2))
                                    skip += 1
                                else:
                                    temp_array.append(utils.execute(0,opcode,utils.look_forward(res,pr["index"])))
                                    skip += 1
                    else:
                        if opcode_skip == 0:
                            temp_array.append(opcode)
                        elif opcode_skip > 0:
                            opcode_skip -= 1
                else:
                    if skip == 0:
                        temp_array.append(opcode)
                    elif skip > 0:
                        skip -= 1

                index +=1
            res = temp_array
            result = res[0]
            groups.pop()
        return result

    def main(self,equation,terms=1,step=1):
        results = []
        i = 1
        while i <= terms:
            parser = utils.parser(equation,evaluate=True,term=i)
            values = utils.decomposer(parser)
            self.data["stack"] = values
            print(values)
            results.append(self.compiler(values))
            i += step
        return results
