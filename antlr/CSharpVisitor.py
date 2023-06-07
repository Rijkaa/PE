# Generated from CSharp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CSharpParser import CSharpParser
else:
    from CSharpParser import CSharpParser

# This class defines a complete generic visitor for a parse tree produced by CSharpParser.

class CSharpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSharpParser#compilation_unit.
    def visitCompilation_unit(self, ctx:CSharpParser.Compilation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#using_directive.
    def visitUsing_directive(self, ctx:CSharpParser.Using_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#namespace_declaration.
    def visitNamespace_declaration(self, ctx:CSharpParser.Namespace_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#namespace_name.
    def visitNamespace_name(self, ctx:CSharpParser.Namespace_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_declaration.
    def visitType_declaration(self, ctx:CSharpParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#class_declaration.
    def visitClass_declaration(self, ctx:CSharpParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#class_member.
    def visitClass_member(self, ctx:CSharpParser.Class_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#method_declaration.
    def visitMethod_declaration(self, ctx:CSharpParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#method_modifier.
    def visitMethod_modifier(self, ctx:CSharpParser.Method_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#method_return_type.
    def visitMethod_return_type(self, ctx:CSharpParser.Method_return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#formal_parameter_list.
    def visitFormal_parameter_list(self, ctx:CSharpParser.Formal_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#formal_parameter.
    def visitFormal_parameter(self, ctx:CSharpParser.Formal_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#method_body.
    def visitMethod_body(self, ctx:CSharpParser.Method_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#field_declaration.
    def visitField_declaration(self, ctx:CSharpParser.Field_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type.
    def visitType(self, ctx:CSharpParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#statement.
    def visitStatement(self, ctx:CSharpParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#block.
    def visitBlock(self, ctx:CSharpParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#if_statement.
    def visitIf_statement(self, ctx:CSharpParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#iteration_statement.
    def visitIteration_statement(self, ctx:CSharpParser.Iteration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#while_statement.
    def visitWhile_statement(self, ctx:CSharpParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#for_statement.
    def visitFor_statement(self, ctx:CSharpParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#for_initializer.
    def visitFor_initializer(self, ctx:CSharpParser.For_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#for_iterator.
    def visitFor_iterator(self, ctx:CSharpParser.For_iteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_variable_declaration.
    def visitLocal_variable_declaration(self, ctx:CSharpParser.Local_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#expression_statement.
    def visitExpression_statement(self, ctx:CSharpParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#return_statement.
    def visitReturn_statement(self, ctx:CSharpParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#expression.
    def visitExpression(self, ctx:CSharpParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#assignment_expression.
    def visitAssignment_expression(self, ctx:CSharpParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#conditional_expression.
    def visitConditional_expression(self, ctx:CSharpParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#logical_or_expression.
    def visitLogical_or_expression(self, ctx:CSharpParser.Logical_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#logical_and_expression.
    def visitLogical_and_expression(self, ctx:CSharpParser.Logical_and_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#equality_expression.
    def visitEquality_expression(self, ctx:CSharpParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#relational_expression.
    def visitRelational_expression(self, ctx:CSharpParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#additive_expression.
    def visitAdditive_expression(self, ctx:CSharpParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:CSharpParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#unary_expression.
    def visitUnary_expression(self, ctx:CSharpParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#primary_expression.
    def visitPrimary_expression(self, ctx:CSharpParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#literal.
    def visitLiteral(self, ctx:CSharpParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#namespace_name_list.
    def visitNamespace_name_list(self, ctx:CSharpParser.Namespace_name_listContext):
        return self.visitChildren(ctx)



del CSharpParser