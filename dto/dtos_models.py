import datetime
from abc import abstractmethod
from dataclasses import dataclass

from base.base_objects import objects
from dto.dtos import db_model
from dto.dtos_model_list import model_list_base


# class to store all DB models - definition of tables and columns/attributes to generate SQL queries for CRUD operations
class model_list(model_list_base):
    # auto-generated - v_models - START

    # auto-generated - v_models - END
    all_models: dict[str, db_model] = {}
    def __init__(self):
        super().__init__()
        print("Creating all DB models")
        self.initialize()

    def generate_rich_view(self, model: db_model) -> str:
        #print(" ************************************************************* ")
        sql = '  <createView  viewName="v_rich_' + model.table_name + '">\n'
        sql = sql + "    select " + model.table_name + ".* \n"
        for fk_column in model.fks:

            fk_table_name = model.fks[fk_column]
            fk_table = self.all_models[fk_table_name]
            for col in fk_table.attr_columns:
                if col != fk_table.key_column_name:
                    sql = sql + "    , _" + fk_column + "." + col + " as " + fk_column + "_" + col
            sql = sql + "\n"
        # "".join("", ) list(map(lambda x: x, fk_table.attr_columns)
        sql = sql + "    from " + model.table_name + " \n"
        for fk_column in model.fks:
            fk_table_name = model.fks[fk_column]
            fk_table = self.all_models[fk_table_name]
            sql = sql + "    left join " + model.fks[fk_column] + " _" + fk_column + " on " +  model.table_name + "." + fk_column  + " = _" + fk_column + "." + fk_table.key_column_name + " \n"
        sql = sql + "  </createView>\n"
        return sql

    def generate_all_rich_views(self) -> list[str]:
        return list(map(lambda m: self.generate_rich_view(m), self.all_models.values()))


    def print_all_rich_views(self):
        lvs = self.generate_all_rich_views()
        for vs in lvs:
            print(vs)

    # handler for closing application
    def close(self):
        print("Closing Models")


# class with all models
db_models = model_list()
