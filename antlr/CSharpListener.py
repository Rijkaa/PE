# Generated from CSharp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CSharpParser import CSharpParser
else:
    from CSharpParser import CSharpParser

# This class defines a complete listener for a parse tree produced by CSharpParser.
class CSharpListener(ParseTreeListener):

    # Enter a parse tree produced by CSharpParser#compilation_unit.
    def enterCompilation_unit(self, ctx:CSharpParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by CSharpParser#compilation_unit.
    def exitCompilation_unit(self, ctx:CSharpParser.Compilation_unitContext):
        pass


    # Enter a parse tree produced by CSharpParser#using_directive.
    def enterUsing_directive(self, ctx:CSharpParser.Using_directiveContext):
        pass

    # Exit a parse tree produced by CSharpParser#using_directive.
    def exitUsing_directive(self, ctx:CSharpParser.Using_directiveContext):
        pass


    # Enter a parse tree produced by CSharpParser#namespace_declaration.
    def enterNamespace_declaration(self, ctx:CSharpParser.Namespace_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#namespace_declaration.
    def exitNamespace_declaration(self, ctx:CSharpParser.Namespace_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#namespace_name.
    def enterNamespace_name(self, ctx:CSharpParser.Namespace_nameContext):
        pass

    # Exit a parse tree produced by CSharpParser#namespace_name.
    def exitNamespace_name(self, ctx:CSharpParser.Namespace_nameContext):
        pass


    # Enter a parse tree produced by CSharpParser#type_declaration.
    def enterType_declaration(self, ctx:CSharpParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#type_declaration.
    def exitType_declaration(self, ctx:CSharpParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_declaration.
    def enterClass_declaration(self, ctx:CSharpParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_declaration.
    def exitClass_declaration(self, ctx:CSharpParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#class_member.
    def enterClass_member(self, ctx:CSharpParser.Class_memberContext):
        pass

    # Exit a parse tree produced by CSharpParser#class_member.
    def exitClass_member(self, ctx:CSharpParser.Class_memberContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_declaration.
    def enterMethod_declaration(self, ctx:CSharpParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_declaration.
    def exitMethod_declaration(self, ctx:CSharpParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_modifier.
    def enterMethod_modifier(self, ctx:CSharpParser.Method_modifierContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_modifier.
    def exitMethod_modifier(self, ctx:CSharpParser.Method_modifierContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_return_type.
    def enterMethod_return_type(self, ctx:CSharpParser.Method_return_typeContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_return_type.
    def exitMethod_return_type(self, ctx:CSharpParser.Method_return_typeContext):
        pass


    # Enter a parse tree produced by CSharpParser#formal_parameter_list.
    def enterFormal_parameter_list(self, ctx:CSharpParser.Formal_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#formal_parameter_list.
    def exitFormal_parameter_list(self, ctx:CSharpParser.Formal_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharpParser#formal_parameter.
    def enterFormal_parameter(self, ctx:CSharpParser.Formal_parameterContext):
        pass

    # Exit a parse tree produced by CSharpParser#formal_parameter.
    def exitFormal_parameter(self, ctx:CSharpParser.Formal_parameterContext):
        pass


    # Enter a parse tree produced by CSharpParser#method_body.
    def enterMethod_body(self, ctx:CSharpParser.Method_bodyContext):
        pass

    # Exit a parse tree produced by CSharpParser#method_body.
    def exitMethod_body(self, ctx:CSharpParser.Method_bodyContext):
        pass


    # Enter a parse tree produced by CSharpParser#field_declaration.
    def enterField_declaration(self, ctx:CSharpParser.Field_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#field_declaration.
    def exitField_declaration(self, ctx:CSharpParser.Field_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#type.
    def enterType(self, ctx:CSharpParser.TypeContext):
        pass

    # Exit a parse tree produced by CSharpParser#type.
    def exitType(self, ctx:CSharpParser.TypeContext):
        pass


    # Enter a parse tree produced by CSharpParser#statement.
    def enterStatement(self, ctx:CSharpParser.StatementContext):
        pass

    # Exit a parse tree produced by CSharpParser#statement.
    def exitStatement(self, ctx:CSharpParser.StatementContext):
        pass


    # Enter a parse tree produced by CSharpParser#block.
    def enterBlock(self, ctx:CSharpParser.BlockContext):
        pass

    # Exit a parse tree produced by CSharpParser#block.
    def exitBlock(self, ctx:CSharpParser.BlockContext):
        pass


    # Enter a parse tree produced by CSharpParser#if_statement.
    def enterIf_statement(self, ctx:CSharpParser.If_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#if_statement.
    def exitIf_statement(self, ctx:CSharpParser.If_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#iteration_statement.
    def enterIteration_statement(self, ctx:CSharpParser.Iteration_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#iteration_statement.
    def exitIteration_statement(self, ctx:CSharpParser.Iteration_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#while_statement.
    def enterWhile_statement(self, ctx:CSharpParser.While_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#while_statement.
    def exitWhile_statement(self, ctx:CSharpParser.While_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#for_statement.
    def enterFor_statement(self, ctx:CSharpParser.For_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#for_statement.
    def exitFor_statement(self, ctx:CSharpParser.For_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#for_initializer.
    def enterFor_initializer(self, ctx:CSharpParser.For_initializerContext):
        pass

    # Exit a parse tree produced by CSharpParser#for_initializer.
    def exitFor_initializer(self, ctx:CSharpParser.For_initializerContext):
        pass


    # Enter a parse tree produced by CSharpParser#for_iterator.
    def enterFor_iterator(self, ctx:CSharpParser.For_iteratorContext):
        pass

    # Exit a parse tree produced by CSharpParser#for_iterator.
    def exitFor_iterator(self, ctx:CSharpParser.For_iteratorContext):
        pass


    # Enter a parse tree produced by CSharpParser#local_variable_declaration.
    def enterLocal_variable_declaration(self, ctx:CSharpParser.Local_variable_declarationContext):
        pass

    # Exit a parse tree produced by CSharpParser#local_variable_declaration.
    def exitLocal_variable_declaration(self, ctx:CSharpParser.Local_variable_declarationContext):
        pass


    # Enter a parse tree produced by CSharpParser#expression_statement.
    def enterExpression_statement(self, ctx:CSharpParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#expression_statement.
    def exitExpression_statement(self, ctx:CSharpParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#return_statement.
    def enterReturn_statement(self, ctx:CSharpParser.Return_statementContext):
        pass

    # Exit a parse tree produced by CSharpParser#return_statement.
    def exitReturn_statement(self, ctx:CSharpParser.Return_statementContext):
        pass


    # Enter a parse tree produced by CSharpParser#expression.
    def enterExpression(self, ctx:CSharpParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#expression.
    def exitExpression(self, ctx:CSharpParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#assignment_expression.
    def enterAssignment_expression(self, ctx:CSharpParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#assignment_expression.
    def exitAssignment_expression(self, ctx:CSharpParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#conditional_expression.
    def enterConditional_expression(self, ctx:CSharpParser.Conditional_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#conditional_expression.
    def exitConditional_expression(self, ctx:CSharpParser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#logical_or_expression.
    def enterLogical_or_expression(self, ctx:CSharpParser.Logical_or_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#logical_or_expression.
    def exitLogical_or_expression(self, ctx:CSharpParser.Logical_or_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#logical_and_expression.
    def enterLogical_and_expression(self, ctx:CSharpParser.Logical_and_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#logical_and_expression.
    def exitLogical_and_expression(self, ctx:CSharpParser.Logical_and_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#equality_expression.
    def enterEquality_expression(self, ctx:CSharpParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#equality_expression.
    def exitEquality_expression(self, ctx:CSharpParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#relational_expression.
    def enterRelational_expression(self, ctx:CSharpParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#relational_expression.
    def exitRelational_expression(self, ctx:CSharpParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#additive_expression.
    def enterAdditive_expression(self, ctx:CSharpParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#additive_expression.
    def exitAdditive_expression(self, ctx:CSharpParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:CSharpParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:CSharpParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#unary_expression.
    def enterUnary_expression(self, ctx:CSharpParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#unary_expression.
    def exitUnary_expression(self, ctx:CSharpParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#primary_expression.
    def enterPrimary_expression(self, ctx:CSharpParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by CSharpParser#primary_expression.
    def exitPrimary_expression(self, ctx:CSharpParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by CSharpParser#literal.
    def enterLiteral(self, ctx:CSharpParser.LiteralContext):
        pass

    # Exit a parse tree produced by CSharpParser#literal.
    def exitLiteral(self, ctx:CSharpParser.LiteralContext):
        pass


    # Enter a parse tree produced by CSharpParser#namespace_name_list.
    def enterNamespace_name_list(self, ctx:CSharpParser.Namespace_name_listContext):
        pass

    # Exit a parse tree produced by CSharpParser#namespace_name_list.
    def exitNamespace_name_list(self, ctx:CSharpParser.Namespace_name_listContext):
        pass



del CSharpParser