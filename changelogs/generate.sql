
-- ----------------------------------------------------------------------------------------------------------------
drop view  v_table_list;

create view  v_table_list as
	select table_name
	, concat('class ', table_name, '_dtos(base_dto):') as dtos_class
	, concat('', table_name, '_dtos') as dtos_class_name
	, concat('class ', table_name, '_write_dto(base_write_dto):') as dto_write_class
	, concat('', table_name, '_write_dto') as dto_write_class_name
	, concat('list[', table_name, '_write_dto]') as dto_write_class_name_list
	, concat('class ', table_name, '_read_dto(base_read_dto, ', table_name, '_write_dto):') as dto_read_class_definition
	, concat('', table_name, '_read_dto') as dto_read_class_name
	, concat('list[', table_name, '_read_dto]') as dto_read_class_name_list
	, concat('', table_name, '_thin_dto') as dto_thin_class_name
	, concat('class ', table_name, '_dao(base_dao):') as dao_class_definition
	, concat('', table_name, '_dao') as dao_class_name
	, concat('class ', table_name, '_service(base_service):') as service_class_definition
	, concat('', table_name, '_service') as service_class_name
	, concat('class ', table_name, '_controller(base_controller):') as controller_class_definition
	, concat('', table_name, '_controller') as controller_class_name
	, '@dataclass(frozen=False)' as dataclass_definition
	, concat('    def get_model(self) -> base_model:') as get_model_method_definition
	, concat('    def get_key(self) -> str:') as get_key_method_definition
	, concat(table_name, '_model') as get_model_object_definition
	, '' as empty_line_definition
	from information_schema.tables
	where table_schema='public' and table_type='BASE TABLE' and table_name not in ('databasechangeloglock', 'databasechangelog')
;


drop view v_column_list;

create view v_column_list as
	select table_name
	 , column_name
	 , concat('self.', column_name) as self_column_name
	 , data_type
	 , is_nullable
	 , ordinal_position
	 , cast(concat(case data_type when 'bigint' then 'int' when 'text' then 'str' when 'timestamp without time zone' then 'datetime.datetime' else 'str' end, ' ', case when is_nullable='YES' then '| None' else '' end) as text) as python_type
	 , cast(concat( column_name, ': ', case data_type when 'bigint' then 'int' when 'text' then 'str' when 'timestamp without time zone' then 'datetime.datetime' else 'str' end, ' ', case when is_nullable='YES' then ' | None' else '' end) as text) as python_definition
	 , cast(concat('    ', column_name, ': ', case data_type when 'bigint' then 'int' when 'text' then 'str' when 'timestamp without time zone' then 'datetime.datetime' else 'str' end, ' ', case when is_nullable='YES' then ' | None' else '' end) as text) as python_definition_class
	 , cast(concat(case when column_name='is_active' then '1' when column_name='custom_attributes' then '"{}"' when column_name='' then ''  when column_name='' then '' when data_type='bigint' then '0' when data_type='text' then '""' when data_type='timestamp without time zone' then 'datetime.datetime.now()' else '""' end) as text) as python_empty_value
	 , cast(concat(case when column_name='is_active' then '1' when column_name='created_by' then '"system"' when column_name='custom_attributes' then '"{}"' when column_name='' then '' when column_name=concat(table_name, '_uid') then 'base_dto.get_random_uid()' when data_type='bigint' then '0' when data_type='text' then '""' when data_type='timestamp without time zone' then 'datetime.datetime.now()' else '""' end) as text) as python_default_value
	 , cast(concat(case when column_name='is_active' then '1' when column_name='created_by' then '"system"' when column_name='custom_attributes' then '"{}"' when column_name='' then '' when column_name=concat(table_name, '_uid') then 'base_dto.get_random_uid()' when data_type='bigint' then '0' when data_type='text' then 'base_dto.get_random_uid()' when data_type='timestamp without time zone' then 'datetime.datetime.now()' else '""' end) as text) as python_random_value
	 , cast(concat('        self.', column_name, ' = ', column_name) as text) as self_set
	 , case when column_name  in ('id', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes') then 1 else 0 end as is_metadata
	 , case when column_name  in ('id', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes') then 1 else 0 end as is_value
	 , case when column_name like '%_uid' and column_name<> concat(table_name, '_uid') then 1 else 0 end as is_fk
	 , case when column_name not in (concat(table_name, '_uid'), 'id', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes') then 1 else 0 end as is_non_key_attribute
	 , case when column_name not in ('id', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes') then 1 else 0 end as is_attribute
	 , case when column_name not in ('id', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by') then 1 else 0 end as is_write
	from information_schema.columns
	where table_schema='public' and table_name not in ('databasechangeloglock', 'databasechangelog') and table_name not like 'v_%'
	order by ordinal_position
;

drop view v_table_column ;

create view v_table_column as
    select t.*
    	-- all columns
        , allcolls.column_list as all_column_list
        , allcolls.column_names_list as all_column_names_list
        , allcolls.column_list_with_type as all_column_list_with_type
        , allcolls.column_dictionary as all_column_dictionary
        , allcolls.column_self_list as all_column_self_list
        , allcolls.column_dto_list as all_column_dto_list
        , allcolls.column_dict_list as all_column_dict_list
        , allcolls.cols_type_definition as all_cols_type_definition
        , allcolls.init_definition as all_init_definition
        , allcolls.python_empty_values as all_python_empty_values
        , allcolls.python_default_values as all_python_default_values
        , allcolls.python_random_values as all_python_random_values
        -- attribute columns
        , attrcols.column_list as attr_column_list
        , attrcols.column_names_list as attr_column_names_list
        , attrcols.column_list_with_type as attr_column_list_with_type
        , attrcols.column_dictionary as attr_column_dictionary
        , attrcols.column_self_list as attr_column_self_list
        , attrcols.column_dto_list as attr_column_dto_list
        , attrcols.column_dict_list as attr_column_dict_list
        , attrcols.cols_type_definition as attr_cols_type_definition
        , attrcols.init_definition as attr_init_definition
        , attrcols.python_empty_values as attrcols_python_empty_values
        , attrcols.python_default_values as attrcols_python_default_values
        , attrcols.python_random_values as attrcols_python_random_values
        -- attribute non key columns
        , attrnonkeycols.column_list as attrnonkey_column_list
        , attrnonkeycols.column_names_list as attrnonkey_column_names_list
        , attrnonkeycols.column_list_with_type as attrnonkey_column_list_with_type
        , attrnonkeycols.column_dictionary as attrnonkey_column_dictionary
        , attrnonkeycols.column_self_list as attrnonkey_column_self_list
        , attrnonkeycols.column_dto_list as attrnonkey_column_dto_list
        , attrnonkeycols.column_dict_list as attrnonkey_column_dict_list
        , attrnonkeycols.cols_type_definition as attrnonkey_cols_type_definition
        , attrnonkeycols.init_definition as attrnonkey_init_definition
        , attrnonkeycols.python_empty_values as attrnonkey_python_empty_values
        , attrnonkeycols.python_default_values as attrnonkey_python_default_values
        , attrnonkeycols.python_random_values as attrnonkey_python_random_values
	from v_table_list t
	 join (
	 	select table_name
	 	 , string_agg(column_name, ', ' order by ordinal_position) as column_list
	 	 , string_agg(concat('''', column_name, ''''), ', ' order by ordinal_position) as column_names_list
	 	 , string_agg(python_definition, ', ' order by ordinal_position) as column_list_with_type
	 	 , concat('[', string_agg(self_column_name, ', ' order by ordinal_position), ']') as column_dictionary
	 	 , concat(string_agg(self_column_name, ', ' order by ordinal_position)) as column_self_list
	 	 , concat(string_agg(concat('dto.', column_name), ', ' order by ordinal_position)) as column_dto_list
	 	 , concat(string_agg(concat('d["', column_name, '"]'), ', ' order by ordinal_position)) as column_dict_list
	 	 , concat('(self, ', string_agg(python_definition, ', ' order by ordinal_position), ')') as cols_type_definition
	 	 , concat('    def __init__(self, ', string_agg(python_definition, ', ' order by ordinal_position), '):') as init_definition
	 	 , string_agg(python_empty_value, ', ' order by ordinal_position) as python_empty_values
	 	 , string_agg(python_default_value, ', ' order by ordinal_position) as python_default_values
	 	 , string_agg(python_random_value, ', ' order by ordinal_position) as python_random_values
		from v_column_list
	 	group by table_name
	 ) allcolls on t.table_name = allcolls.table_name
	 join (
		select table_name
		 , string_agg(column_name, ', ' order by ordinal_position) as column_list
	 	 , string_agg(concat('''', column_name, ''''), ', ' order by ordinal_position) as column_names_list
	 	 , string_agg(python_definition, ', ' order by ordinal_position) as column_list_with_type
	 	 , concat('[', string_agg(self_column_name, ', ' order by ordinal_position), ']') as column_dictionary
	 	 , concat(string_agg(self_column_name, ', ' order by ordinal_position)) as column_self_list
	 	 , concat(string_agg(concat('dto.', column_name), ', ' order by ordinal_position)) as column_dto_list
	 	 , concat(string_agg(concat('d["', column_name, '"]'), ', ' order by ordinal_position)) as column_dict_list
	 	 , concat('(self, ', string_agg(python_definition, ', ' order by ordinal_position), ')') as cols_type_definition
		 , concat('    def __init__(self, ', string_agg(python_definition, ', ' order by ordinal_position), '):') as init_definition
	 	 , string_agg(python_empty_value, ', ' order by ordinal_position) as python_empty_values
	 	 , string_agg(python_default_value, ', ' order by ordinal_position) as python_default_values
	 	 , string_agg(python_random_value, ', ' order by ordinal_position) as python_random_values
		from v_column_list
		where is_attribute=1
		group by table_name
	 ) attrcols on t.table_name = attrcols.table_name
	 join (
		select table_name
		 , string_agg(column_name, ', ' order by ordinal_position) as column_list
	 	 , string_agg(concat('''', column_name, ''''), ', ' order by ordinal_position) as column_names_list
	 	 , string_agg(python_definition, ', ' order by ordinal_position) as column_list_with_type
	 	 , concat('[', string_agg(self_column_name, ', ' order by ordinal_position), ']') as column_dictionary
	 	 , concat(string_agg(self_column_name, ', ' order by ordinal_position)) as column_self_list
	 	 , concat(string_agg(concat('dto.', column_name), ', ' order by ordinal_position)) as column_dto_list
	 	 , concat(string_agg(concat('d["', column_name, '"]'), ', ' order by ordinal_position)) as column_dict_list
	 	 , concat('(self, ', string_agg(python_definition, ', ' order by ordinal_position), ')') as cols_type_definition
		 , concat('    def __init__(self, ', string_agg(python_definition, ', ' order by ordinal_position), '):') as init_definition
	 	 , string_agg(python_empty_value, ', ' order by ordinal_position) as python_empty_values
	 	 , string_agg(python_default_value, ', ' order by ordinal_position) as python_default_values
	 	 , string_agg(python_random_value, ', ' order by ordinal_position) as python_random_values
		from v_column_list
		where is_non_key_attribute=1
		group by table_name
	 ) attrnonkeycols on t.table_name = attrnonkeycols.table_name
;


select * from information_schema.columns

select *
from v_table_list
;
select *
from v_column_list
;
select *
from v_table_column
;


-- models
select concat(table_name, '_model = base_model(''', table_name, ''', [',  all_column_names_list, '], [', attr_column_names_list, '])'), *
from v_table_column
;

-- write_dto classes
select *
from (
select table_name, 100 as ordinal_position, dataclass_definition as python from v_table_list
union all select table_name, 110 as ordinal_position, dto_write_class as python from v_table_list
union all select table_name, 200+ordinal_position , python_definition_class from v_column_list where is_attribute=1

union all select table_name, 400 as ordinal_position, concat('    def __init__(self, ',  attr_column_list_with_type , ', custom_attributes: str = "{}"):') from v_table_column
union all select table_name, 500+ordinal_position , self_set from v_column_list where is_attribute=1
union all select table_name, 599 as ordinal_position, concat('        self.custom_attributes = custom_attributes') from v_table_column

union all select table_name, 1110 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1120 as ordinal_position, '    def empty_write(cls):' as python from v_table_list
union all select table_name, 1130 as ordinal_position, concat('        return cls(', attrcols_python_empty_values, ')') as python from v_table_column
union all select table_name, 1210 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1220 as ordinal_position, '    def default_write(cls):' as python from v_table_list
union all select table_name, 1230 as ordinal_position, concat('        return cls(', attrcols_python_default_values, ')') as python from v_table_column
union all select table_name, 1310 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1320 as ordinal_position, '    def random_write(cls):' as python from v_table_list
union all select table_name, 1330 as ordinal_position, concat('        return cls(', attrcols_python_random_values, ')') as python from v_table_column

union all select table_name, 1410 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1420 as ordinal_position, concat('    def new_write(cls, ', attr_column_list_with_type , '):') as python from v_table_column
union all select table_name, 1430 as ordinal_position, concat('        return cls(', attr_column_list, ')') as python from v_table_column

union all select table_name, 1510 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1520 as ordinal_position, concat('    def new_write_random_uid(cls, ', attrnonkey_column_list_with_type , '):') as python from v_table_column
union all select table_name, 1530 as ordinal_position, concat('        return cls(base_dto.get_random_uid(), ', attrnonkey_column_list, ')') as python from v_table_column

union all select table_name, 1810 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1811 as ordinal_position, '    def get_class_model(cls) -> base_model:' as python from v_table_list
union all select table_name, 1812 as ordinal_position, concat('        return ', table_name, '_model') as python from v_table_list

union all select table_name, 1821 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1822 as ordinal_position, '    def from_dictionary(cls, d: dict[str, any]):' as python from v_table_list
union all select table_name, 1823 as ordinal_position, concat('        return cls(', attr_column_dict_list, ')') as python from v_table_column

union all select table_name, 1900 , concat('    def to_write_dict(self) -> dict:') from v_table_list
union all select table_name, 1901 , concat('        return asdict(self)') from v_table_list

union all select table_name, 2120 as ordinal_position, '    def clone_write(self):' as python from v_table_list
union all select table_name, 2130 as ordinal_position, concat('        return ', dto_write_class_name , '(', attr_column_self_list, ', self.custom_attributes)') as python from v_table_column
union all select table_name, 2210 as ordinal_position, '    def clone_write_new_uid(self):' as python from v_table_list
union all select table_name, 2220 as ordinal_position, concat('        return ', dto_write_class_name , '(base_dto.get_random_uid(), ', attrnonkey_column_self_list, ', self.custom_attributes)') as python from v_table_column
union all select table_name, 2310 as ordinal_position, '    def clone_with_uid(self, uid: str):' as python from v_table_list
union all select table_name, 2320 as ordinal_position, concat('        return ', dto_write_class_name , '(uid, ', attrnonkey_column_self_list, ', self.custom_attributes)') as python from v_table_column

union all select table_name, 3110 as ordinal_position, '    def get_model(self) -> base_model:' as python from v_table_list
union all select table_name, 3120 as ordinal_position, concat('        return ', table_name, '_model') as python from v_table_list
union all select table_name, 3210 as ordinal_position, '    def get_key(self) -> str:' as python from v_table_list
union all select table_name, 3211 as ordinal_position, concat('        return self.', table_name, '_uid') as python from v_table_list

union all select table_name, 3221 as ordinal_position, '    def get_uid(self) -> str:' as python from v_table_list
union all select table_name, 3222 as ordinal_position, concat('        return self.', table_name, '_uid') as python from v_table_list

union all select table_name, 3310 as ordinal_position, '    def get_list_values(self) -> list[any]:' as python from v_table_list
union all select table_name, 3311 as ordinal_position, concat('        return [', attr_column_self_list, ', self.custom_attributes]') as python from v_table_column

union all select table_name, 3321 as ordinal_position, '    def get_list_values_no_custom(self) -> list[any]:' as python from v_table_list
union all select table_name, 3322 as ordinal_position, concat('        return [', attr_column_self_list, ']') as python from v_table_column

union all select table_name, 3331 as ordinal_position, '    def get_list_write_update(self, updated_by: str) -> list[any]:' as python from v_table_list
union all select table_name, 3332 as ordinal_position, concat('        return [', attrnonkey_column_self_list, ', self.custom_attributes, updated_by, self.', table_name, '_uid]') as python from v_table_column

union all select table_name, 3341 as ordinal_position, '    def get_list_write_insert(self, created_by: str) -> list[any]:' as python from v_table_list
union all select table_name, 3342 as ordinal_position, concat('        return [self.', table_name, '_uid, ', attrnonkey_column_self_list, ', created_by, created_by, self.custom_attributes]') as python from v_table_column

union all select table_name, 3410 as ordinal_position, '    def get_nonkey_values(self) -> list[any]:' as python from v_table_list
union all select table_name, 3411 as ordinal_position, concat('        return [', attrnonkey_column_self_list, ']') as python from v_table_column

union all select table_name, 3420 as ordinal_position, '    def get_nonkey_values_with_custom(self) -> list[any]:' as python from v_table_list
union all select table_name, 3421 as ordinal_position, concat('        return [', attrnonkey_column_self_list, ', self.custom_attributes]') as python from v_table_column

union all select table_name, 3431 as ordinal_position, '    def to_json_write(self) -> str:' as python from v_table_list
union all select table_name, 3432 as ordinal_position, concat('        return json.dumps(self.to_write_dict())') as python from v_table_column

union all select table_name, 3510 as ordinal_position, '    def compare_uid(self, obj: base_write_dto) -> bool:' as python from v_table_list
union all select table_name, 3520 as ordinal_position, concat('        return self.get_key() == obj.get_key()') as python from v_table_column

union all select table_name, 4110 as ordinal_position, '    def update_uid(self, uid: str):' as python from v_table_list
union all select table_name, 4111 as ordinal_position, concat('        self.', table_name ,'_uid = uid') as python from v_table_list

union all select table_name, 4202 as ordinal_position, concat('    def update_uid_attributes(self, ', attr_column_list_with_type  , '):') as python from v_table_column
union all select table_name, 4203+ordinal_position as ordinal_position, concat('        self.', column_name, ' = ', column_name , '') as python from v_column_list where is_attribute=1

union all select table_name, 4302 as ordinal_position, concat('    def update_attributes(self, ', attrnonkey_column_list_with_type , '):') as python from v_table_column
union all select table_name, 4303+ordinal_position as ordinal_position, concat('        self.', column_name, ' = ', column_name , '') as python from v_column_list where is_non_key_attribute=1

--union all select table_name, 2700 as ordinal_position, concat('    def to_read(self) -> ', table_name, '_read_dto:') as python from v_table_list
--union all select table_name, 2800 as ordinal_position, concat('        return ', table_name, '_read_dto(0, ', attr_column_self_list, ', "", 0, 1, datetime.now(), "system", datetime.now(), "system", None, None, "{}")') as python from v_table_column

union all select table_name, 99900 , empty_line_definition from v_table_list
union all select table_name, 99901 , empty_line_definition from v_table_list
) x order by x.table_name, x.ordinal_position
;


-- thin_dto classes - TO BE DONE
select *
from (
select table_name, 100 as ordinal_position, dataclass_definition as python from v_table_list
union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_thin_dto(base_dto):') as python from v_table_list

union all select table_name, 201 , concat('    ', table_name , '_uid: str') from v_table_list
union all select table_name, 202 , concat('    row_guid: str') from v_table_list
union all select table_name, 203 , concat('    is_active: int') from v_table_list
union all select table_name, 204 , concat('    def __init__(self, ', table_name , '_uid: str , row_guid: str , is_active: int):') from v_table_list
union all select table_name, 205 , concat('        self.', table_name , '_uid = ', table_name , '_uid') from v_table_list
union all select table_name, 206 , concat('        self.row_guid = row_guid') from v_table_list
union all select table_name, 207 , concat('        self.is_active = is_active') from v_table_list

union all select table_name, 99900 , empty_line_definition from v_table_list
union all select table_name, 99901 , empty_line_definition from v_table_list
) x order by x.table_name, x.ordinal_position
;

-- read_dto classes
select *
from (
select table_name, 100 as ordinal_position, dataclass_definition as python from v_table_list
union all select table_name, 110 as ordinal_position, dto_read_class_definition as python from v_table_list
union all select table_name, 200+ordinal_position , python_definition_class from v_column_list
union all select table_name, 400 as ordinal_position, all_init_definition from v_table_column
union all select table_name, 500+ordinal_position , self_set from v_column_list

union all select table_name, 1110 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1120 as ordinal_position, '    def empty_read(cls):' as python from v_table_list
union all select table_name, 1130 as ordinal_position, concat('        return cls(0, ', attrcols_python_empty_values, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_table_column
union all select table_name, 1210 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1220 as ordinal_position, '    def default_read(cls):' as python from v_table_list
union all select table_name, 1230 as ordinal_position, concat('        return cls(0, ', attrcols_python_default_values, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_table_column
union all select table_name, 1310 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1320 as ordinal_position, '    def random_read(cls):' as python from v_table_list
union all select table_name, 1330 as ordinal_position, concat('        return cls(0, ', attrcols_python_random_values, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_table_column

union all select table_name, 1410 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1420 as ordinal_position, concat('    def new_read_default(cls, ', attr_column_list_with_type , '):') as python from v_table_column
union all select table_name, 1430 as ordinal_position, concat('        return cls(0, ', attr_column_list, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_table_column

union all select table_name, 1510 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1520 as ordinal_position, concat('    def new_read_full(cls, ', all_column_list_with_type , '):') as python from v_table_column
union all select table_name, 1530 as ordinal_position, concat('        return cls(', all_column_list, ')') as python from v_table_column

union all select table_name, 1610 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1620 as ordinal_position, concat('    def from_write(cls, dto: ', dto_write_class_name, '):') as python from v_table_column
union all select table_name, 1630 as ordinal_position, concat('        return cls(0, ', attr_column_dto_list, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)') as python from v_table_column

union all select table_name, 1710 as ordinal_position, '    def clone_read(self):' as python from v_table_list
union all select table_name, 1711 as ordinal_position, concat('        return ', dto_read_class_name , '(', all_column_self_list, ')') as python from v_table_column
--union all select table_name, 1720 as ordinal_position, '    def clone_read_new_uid(self):' as python from v_table_list
--union all select table_name, 1721 as ordinal_position, concat('        return ', dto_read_class_name , '(base_dto.get_random_uid(), ', attrnonkey_column_self_list, ')') as python from v_table_column
--union all select table_name, 1730 as ordinal_position, '    def clone_read_with_uid(self, uid: str):' as python from v_table_list
--union all select table_name, 1731 as ordinal_position, concat('        return ', dto_read_class_name , '(uid, ', attrnonkey_column_self_list, ')') as python from v_table_column

union all select table_name, 1721 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1722 as ordinal_position, '    def from_dictionary(cls, d: dict[str, any]):' as python from v_table_list
union all select table_name, 1723 as ordinal_position, concat('        return cls(', all_column_dict_list, ')') as python from v_table_column

union all select table_name, 1731 , concat('    def to_read_dict(self) -> dict:') from v_table_list
union all select table_name, 1732 , concat('        return asdict(self)') from v_table_list

union all select table_name, 1800 as ordinal_position, concat('    def to_write(self) -> ', dto_write_class_name, ':') as python from v_table_list
union all select table_name, 1801 as ordinal_position, concat('        return ', dto_write_class_name, '(', attr_column_self_list, ', self.custom_attributes)') as python from v_table_column

union all select table_name, 1810 as ordinal_position, concat('    def to_thin(self) -> ', table_name, '_thin_dto:') as python from v_table_list
union all select table_name, 1811 as ordinal_position, concat('        return ', table_name, '_thin_dto(self.', table_name, '_uid, self.row_guid, self.is_active)') as python from v_table_column

union all select table_name, 1910 as ordinal_position, '    def touch(self, updated_by: str = "system"):' as python from v_table_list
union all select table_name, 1911 as ordinal_position, concat('        self.last_updated_date = datetime.datetime.now()') as python from v_table_list
union all select table_name, 1912 as ordinal_position, concat('        self.last_updated_by = updated_by') as python from v_table_list
union all select table_name, 1913 as ordinal_position, concat('        self.row_version = self.row_version+1') as python from v_table_list

union all select table_name, 2300 as ordinal_position, '    def get_list_all_values(self) -> list[any]:' as python from v_table_list
union all select table_name, 2301 as ordinal_position, concat('        return ', all_column_dictionary, '') as python from v_table_column

union all select table_name, 2310 as ordinal_position, '    def get_list_update_values(self, updated_by: str) -> list[any]:' as python from v_table_list
union all select table_name, 2311 as ordinal_position, concat('        return [', attrnonkey_column_self_list, ', self.custom_attributes, updated_by, self.', table_name, '_uid]') as python from v_table_column

union all select table_name, 2400 as ordinal_position, '    def is_older_than(self, dt: datetime.datetime) -> bool:' as python from v_table_list
union all select table_name, 2410 as ordinal_position, concat('        return self.created_date < dt') as python from v_table_column
union all select table_name, 2500 as ordinal_position, '    def is_newer_than(self, dt: datetime.datetime) -> bool:' as python from v_table_list
union all select table_name, 2510 as ordinal_position, concat('        return self.created_date > dt') as python from v_table_column

union all select table_name, 2600 as ordinal_position, '    def to_json_read(self) -> str:' as python from v_table_list
union all select table_name, 2610 as ordinal_position, concat('        return json.dumps(self.to_read_dict())') as python from v_table_column

union all select table_name, 99900 , empty_line_definition from v_table_list
union all select table_name, 99901 , empty_line_definition from v_table_list
) x order by x.table_name, x.ordinal_position
;



union all select table_name, 562 , concat('') from v_table_list
union all select table_name, 562 , concat('') from v_table_list
union all select table_name, 562 , concat('') from v_table_list
union all select table_name, 562 , concat('') from v_table_list
union all select table_name, 562 , concat('') from v_table_list
union all select table_name, 562 , concat('') from v_table_list



-- read_dtos classes
select *
from (
select table_name, 100 as ordinal_position, dataclass_definition as python from v_table_list
union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_read_dtos(base_dtos):') as python from v_table_list
union all select table_name, 210 , concat('    dtos: list[', table_name , '_read_dto]') from v_table_list
union all select table_name, 220 , concat('    def __init__(self, dtos: list[', table_name , '_read_dto]):') from v_table_list
union all select table_name, 230 , '        self.dtos = dtos' from v_table_list

union all select table_name, 300 , '    @classmethod' from v_table_list
union all select table_name, 301 , '    def empty_list(cls):' from v_table_list
union all select table_name, 302 , '        return cls(list())' from v_table_list

union all select table_name, 310 , '    @classmethod' from v_table_list
union all select table_name, 311 , concat('    def from_list(cls, dtos: list[', table_name , '_read_dto]):') from v_table_list
union all select table_name, 312 , '        return cls(dtos)' from v_table_list

union all select table_name, 320 , '    @classmethod' from v_table_list
union all select table_name, 321 , concat('    def from_object(cls, dto: ', table_name , '_read_dto):') from v_table_list
union all select table_name, 322 , '        return cls(list(dto))' from v_table_list

union all select table_name, 330 , '    @classmethod' from v_table_list
union all select table_name, 331 , concat('    def from_lists(cls, dtos1: list[', table_name , '_read_dto], dtos2: list[', table_name , '_read_dto]):') from v_table_list
union all select table_name, 332 , '        return cls(dtos1 + dtos2)' from v_table_list

union all select table_name, 501 , concat('    def get_active(self):') from v_table_list
union all select table_name, 502 , concat('        return ', table_name, '_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))') from v_table_list

union all select table_name, 511 , concat('    def get_inactive(self):') from v_table_list
union all select table_name, 512 , concat('        return ', table_name, '_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))') from v_table_list

union all select table_name, 521 , concat('    def get_write_dtos(self) -> list[', table_name , '_write_dto]:') from v_table_list
union all select table_name, 522 , concat('        return list(filter(lambda x: x.to_write() != 1, self.dtos))') from v_table_list

union all select table_name, 531 , concat('    def get_write_dicts(self) -> list[dict]:') from v_table_list
union all select table_name, 532 , concat('        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))') from v_table_list

union all select table_name, 541 , concat('    def get_read_dicts(self) -> list[dict]:') from v_table_list
union all select table_name, 542 , concat('        return list(map(lambda x: x.to_write_dict(), self.dtos))') from v_table_list

union all select table_name, 551 , concat('    def find_by_uid(self, uid: str) -> ', table_name, '_read_dto | None:') from v_table_list
union all select table_name, 552 , concat('        found_dtos = list(filter(lambda x: x.', table_name, '_uid == uid, self.dtos))') from v_table_list
union all select table_name, 553 , concat('        if (len(found_dtos)>0):') from v_table_list
union all select table_name, 554 , concat('            return found_dtos[0]') from v_table_list
union all select table_name, 555 , concat('        else:') from v_table_list
union all select table_name, 556 , concat('            return None') from v_table_list

union all select table_name, 1001 , concat('    def get_first(self) -> ', table_name, '_read_dto | None:') from v_table_list
union all select table_name, 1002 , concat('        if len(self.dtos) > 0:') from v_table_list
union all select table_name, 1003 , concat('            return self.dtos[0]') from v_table_list
union all select table_name, 1004 , concat('        else:') from v_table_list
union all select table_name, 1005 , concat('            return None') from v_table_list

union all select table_name, 99900 , empty_line_definition from v_table_list
union all select table_name, 99901 , empty_line_definition from v_table_list
) x order by x.table_name, x.ordinal_position
;

union all select table_name, 1004 , concat('') from v_table_list
union all select table_name, 1005 , concat('') from v_table_list
union all select table_name, 1006 , concat('') from v_table_list
union all select table_name, 1007 , concat('') from v_table_list



-- write_dtos classes
select *
from (
select table_name, 100 as ordinal_position, dataclass_definition as python from v_table_list
union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_write_dtos(base_dtos):') as python from v_table_list
union all select table_name, 210 , concat('    dtos: list[', table_name , '_write_dto]') from v_table_list
union all select table_name, 220 , concat('    def __init__(self, dtos: list[', table_name , '_write_dto]):') from v_table_list
union all select table_name, 230 , '        self.dtos = dtos' from v_table_list

union all select table_name, 300 , '    @classmethod' from v_table_list
union all select table_name, 301 , '    def empty_list(cls):' from v_table_list
union all select table_name, 302 , '        return cls(list())' from v_table_list

union all select table_name, 310 , '    @classmethod' from v_table_list
union all select table_name, 311 , concat('    def from_list(cls, dtos: list[', table_name , '_write_dto]):') from v_table_list
union all select table_name, 312 , '        return cls(dtos)' from v_table_list

union all select table_name, 320 , '    @classmethod' from v_table_list
union all select table_name, 321 , concat('    def from_object(cls, dto: ', table_name , '_write_dto):') from v_table_list
union all select table_name, 322 , '        return cls(list(dto))' from v_table_list

union all select table_name, 330 , '    @classmethod' from v_table_list
union all select table_name, 331 , concat('    def from_lists(cls, dtos1: list[', table_name , '_write_dto], dtos2: list[', table_name , '_write_dto]):') from v_table_list
union all select table_name, 332 , '        return cls(dtos1 + dtos2)' from v_table_list

union all select table_name, 531 , concat('    def get_write_dicts(self) -> list[dict]:') from v_table_list
union all select table_name, 532 , concat('        return list(map(lambda x: x.to_write_dict(), self.dtos))') from v_table_list

union all select table_name, 551 , concat('    def find_by_uid(self, uid: str) -> ', table_name, '_write_dto | None:') from v_table_list
union all select table_name, 552 , concat('        found_dtos = list(filter(lambda x: x.', table_name, '_uid == uid, self.dtos))') from v_table_list
union all select table_name, 553 , concat('        if (len(found_dtos)>0):') from v_table_list
union all select table_name, 554 , concat('            return found_dtos[0]') from v_table_list
union all select table_name, 555 , concat('        else:') from v_table_list
union all select table_name, 556 , concat('            return None') from v_table_list

union all select table_name, 561 , concat('    def map_by_uid(self) -> dict[str, ', table_name , '_write_dto]:') from v_table_list
union all select table_name, 562 , concat('        res = {}') from v_table_list
union all select table_name, 563 , concat('        for dto in self.dtos:') from v_table_list
union all select table_name, 564 , concat('            res[dto.', table_name , '_uid] = dto') from v_table_list
union all select table_name, 565 , concat('        return res') from v_table_list

union all select table_name, 99900 , empty_line_definition from v_table_list
union all select table_name, 99901 , empty_line_definition from v_table_list
) x order by x.table_name, x.ordinal_position
;


-- dao classes
select *
from (
select table_name, 1000 as ordinal_position, concat('class ', table_name, '_dao(base_dao):') from v_table_list
union all select table_name, 1001 , concat('    def __init__(self):') from v_table_list
union all select table_name, 1002 , concat('        print("Starting ', table_name, ' DAO")') from v_table_list
union all select table_name, 1003 , concat('    def get_model(self) -> base_model:') from v_table_list
union all select table_name, 1004 , concat('        return ', table_name, '_model') from v_table_list

union all select table_name, 1005 , concat('    def get_items(self, sql: str) -> list[', table_name, '_read_dto]:') from v_table_list
union all select table_name, 1006 , concat('        return list(map(lambda r: ', table_name, '_read_dto(*r), self.get_objects(sql)))') from v_table_list
union all select table_name, 1007 , concat('    def get_items_with_params(self, sql: str, params: Iterable) -> list[', table_name, '_read_dto]:') from v_table_list
union all select table_name, 1008 , concat('        return list(map(lambda r: ', table_name, '_read_dto(*r), self.get_objects_by_params(sql, params)))') from v_table_list

union all select table_name, 1020 , concat('    def get_items_write(self, sql: str) -> list[', table_name, '_write_dto]:') from v_table_list
union all select table_name, 1021 , concat('        return list(map(lambda r: ', table_name, '_write_dto(*r), self.get_objects(sql)))') from v_table_list
union all select table_name, 1022 , concat('    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[', table_name, '_write_dto]:') from v_table_list
union all select table_name, 1023 , concat('        return list(map(lambda r: ', table_name, '_write_dto(*r), self.get_objects_by_params(sql, params)))') from v_table_list

union all select table_name, 1120 , concat('    def get_items_all(self, n: int = 1000) -> ', table_name, '_read_dtos:') from v_table_list
union all select table_name, 1121 , concat('        return ', table_name, '_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))') from v_table_list
union all select table_name, 1122 , concat('    def get_items_active(self, n: int = 1000) -> ', table_name, '_read_dtos:') from v_table_list
union all select table_name, 1123 , concat('        return ', table_name, '_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))') from v_table_list
union all select table_name, 1130 , concat('    def get_items_all_latest(self, n: int = 1000) -> ', table_name, '_read_dtos:') from v_table_list
union all select table_name, 1131 , concat('        return ', table_name, '_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))') from v_table_list
union all select table_name, 1132 , concat('    def get_items_active_latest(self, n: int = 1000) -> ', table_name, '_read_dtos:') from v_table_list
union all select table_name, 1133 , concat('        return ', table_name, '_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))') from v_table_list

union all select table_name, 1140 , concat('    def get_items_write_all(self, n: int = 1000) -> ', table_name, '_write_dtos:') from v_table_list
union all select table_name, 1141 , concat('        return ', table_name, '_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))') from v_table_list
union all select table_name, 1142 , concat('    def get_items_write_active(self, n: int = 1000) -> ', table_name, '_write_dtos:') from v_table_list
union all select table_name, 1143 , concat('        return ', table_name, '_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))') from v_table_list
union all select table_name, 1150 , concat('    def get_items_write_all_latest(self, n: int = 1000) -> ', table_name, '_write_dtos:') from v_table_list
union all select table_name, 1151 , concat('        return ', table_name, '_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))') from v_table_list
union all select table_name, 1152 , concat('    def get_items_write_active_latest(self, n: int = 1000) -> ', table_name, '_write_dtos:') from v_table_list
union all select table_name, 1153 , concat('        return ', table_name, '_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))') from v_table_list

union all select table_name, 1240 , concat('    def get_item_by_uid(self, uid: str) -> ', table_name, '_read_dto | None:') from v_table_list
union all select table_name, 1241 , concat('        return ', table_name, '_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()') from v_table_list
union all select table_name, 1242 , concat('    def get_item_by_id(self, id: int) -> ', table_name, '_read_dto | None:') from v_table_list
union all select table_name, 1243 , concat('        return ', table_name, '_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()') from v_table_list

union all select table_name, 1250 , concat('    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> ', table_name, '_read_dtos:') from v_table_list
union all select table_name, 1251 , concat('        return ', table_name, '_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))') from v_table_list
union all select table_name, 1252 , concat('    def get_uids(self, n: int = 1000) -> list[str]:') from v_table_list
union all select table_name, 1253 , concat('        return self.get_column_values_all(self.get_model().get_select_all_keys(n))') from v_table_list
union all select table_name, 1254 , concat('    def get_guids(self, n: int = 1000) -> list[str]:') from v_table_list
union all select table_name, 1255 , concat('        return self.get_column_values_all(self.get_model().get_select_all_guids(n))') from v_table_list

union all select table_name, 1360 , concat('    def count_all(self) -> int:') from v_table_list
union all select table_name, 1361 , concat('        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())') from v_table_list
union all select table_name, 1363 , concat('    def count_active(self) -> int:') from v_table_list
union all select table_name, 1364 , concat('        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())') from v_table_list
union all select table_name, 1365 , concat('    def count_by_any_column(self, col_name: str, col_value: any) -> int:') from v_table_list
union all select table_name, 1366 , concat('        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))') from v_table_list

union all select table_name, 1410 , concat('    def insert_dtos(self, dtos: list[', table_name, '_write_dto], created_by: str):') from v_table_list
union all select table_name, 1411 , concat('        self.insert_many(dtos, created_by)') from v_table_list

union all select table_name, 1420 , concat('    def insert_write_dtos(self, dtos: ', table_name, '_write_dtos, created_by: str):') from v_table_list
union all select table_name, 1421 , concat('        self.insert_dtos(dtos.dtos, created_by)') from v_table_list

union all select table_name, 1430 , concat('    def insert_read_dtos(self, dtos: ', table_name, '_read_dtos, created_by: str):') from v_table_list
union all select table_name, 1431 , concat('        self.insert_dtos(dtos.get_write_dtos(), created_by)') from v_table_list

union all select table_name, 1440 , concat('    def delete_logical_dtos(self, dtos: list[', table_name, '_write_dto], removed_by: str):') from v_table_list
union all select table_name, 1441 , concat('        uids = list(map(lambda dto: dto.get_uid(), dtos))') from v_table_list
union all select table_name, 1442 , concat('        return self.delete_logical_by_uids(uids, removed_by)') from v_table_list

union all select table_name, 1450 , concat('    def delete_logical_write_dtos(self, dtos: ', table_name, '_write_dtos, removed_by: str):') from v_table_list
union all select table_name, 1451 , concat('        return self.delete_logical_dtos(dtos.dtos, removed_by)') from v_table_list

union all select table_name, 99900 , empty_line_definition from v_table_list
union all select table_name, 99901 , empty_line_definition from v_table_list
) x order by x.table_name, x.ordinal_position
;






-- models
select concat(table_name, '_dao_instance = ', table_name,'_dao()')
from v_table_column
;





union all select table_name, 1460 , concat('') from v_table_list
union all select table_name, 1461 , concat('') from v_table_list


union all select table_name, 1580 , concat('') from v_table_list
union all select table_name, 1581 , concat('') from v_table_list


union all select table_name, 1004 , concat('') from v_table_list
union all select table_name, 1005 , concat('') from v_table_list
union all select table_name, 1006 , concat('') from v_table_list
union all select table_name, 1007 , concat('') from v_table_list





union all
















union all select table_name, 1110 as ordinal_position, '    @classmethod' as python from v_table_list
union all select table_name, 1120 as ordinal_position, '    def empty_read(cls):' as python from v_table_list
union all select table_name, 1130 as ordinal_position, concat('        return cls(0, ', attrcols_python_empty_values, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_table_column



    def get_list_all_values(self) -> list[any]:
        return [self.id, self.account_division_uid, self.division_name, self.division_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def is_older_than(self, dt: datetime) -> bool:
        return self.created_date > dt


    @classmethod
    def from_write(cls, account_division_uid: str, division_name: str, division_description: str):
        return cls(0, account_division_uid, division_name, division_description, "", 0, 1, datetime.now(), "system", datetime.now(), "system", None, None, "{}")



select *
from information_schema.table_constraints tc
where constraint_schema ='public'

SELECT
  tc.constraint_name,
  tc.constraint_type,
  tc.table_name,
  kcu.column_name,
  ccu.table_name AS foreign_table_name,
  ccu.column_name AS foreign_column_name
FROM information_schema.table_constraints AS tc
 JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name
 JOIN information_schema.constraint_column_usage AS ccu ON ccu.constraint_name = tc.constraint_name
WHERE constraint_type = 'FOREIGN KEY'


    def is_active(self) -> bool:
        return self.is_active == 1

select * from v_table_list

-- service classes
t_service
	insert_all()

-- controller classes
t_controller(base_controller)

	@app.route('/api/token', methods=['GET'])
	@app.route('/api/userinfo', methods=['GET'])
	@app.route('/api/userinfo', methods=['GET'])


	def get_t_by_uid(uid):
		t_dao_instance.get_rows()
	   return jsonify({'tasks': clients})

	@app.route('/api/t-list', methods=['GET'])
	def get_t_by_uid(uid):
		t_dao_instance.get_rows()
	   return jsonify({'tasks': clients})

	@app.route('/api/t-active', methods=['GET'])
	@app.route('/api/t-removed', methods=['GET'])

	@app.route('/api/t-last', methods=['GET'])
	def get_t_last()

	@app.route('/api/t', methods=['POST'])
	-- wrap with security somehow
	def get_t_last()









y(y_uid)
z(z_uid)
t(t_id, t_uid, t_name, y_uid, z_uid, row_guid, is_active, created_by, created_date, last_updated_by, last_updated_date, row_version )
t_history(t_id, t_uid, t_name, y_uid, z_uid, row_guid, is_active, created_by, created_date, last_updated_by, last_updated_date, row_version, inserted_row_date)
insert into t_history() select * from t where ...
insert into t() values (?, ?, ?, ?, ?, ?) on conflict () do nothing;
insert into t() values (?, ?, ?, ?, ?, ?) on conflict () do update set ....

COLUMNS
metadata=id, row_guid, is_active, created_by, created_date, last_updated_by, last_updated_date, custom_attributes
uid=t_uid
values=some_name, other_name
attributes=t_uid, some_name, other_name
write_columns={attribute}, custom_attributes
name=some_name
fks=some_table_uid, other_table_uid,
----
all_columns=id, ...., row_guid, is_active, ...
uid_column=t_uid
fk_columns
name_column=t_name


create view v_t as
select *
from t t
join y y on t.y_uid=y.y_uid
join z z on t.z_uid=z.z_uid
;
-- ------------------------------------------------------------------------------------------------------------

DB
id, t_uid, {*}, row_guid, is_active, created_by, created_date, last_updated_by, last_updated_date, row_version: int, custom_attributes
* = custom_col, ...

DTOs
	base_dto
	custom_attributes

base_write_dto(base_dto)
	+custom_attributes
	abstract get_key()
	abstract get_name()
	abstract get_uid()
	set_custom_attributes(dict)
	add_custom_attribute(name, value)
	get_custom_attributes_as_dict(): dict
	get_custom_attributes_as_json(): str
	clear_custom_attributes()
	remove_custom_attribute()
	get_custom_attributes_names(): list[str]
	get_custom_attributes()
	get_custom_attribute(attr_name)

base_read_dto(base_dto)
	+id, row_guid, is_active, created_by, created_date, last_updated_by, last_updated_date, row_version, custom_attributes
	get_id()
	get_created_date()
	get_created_date_as_int()
	get_last_upadted_date()
	get_last_upadted_date_as_long()
	get_as_dictionary(): dict
	get_as_json(): str
	get_as_string(): str
	get_write_table(): list[any]
	is_created_later_than(datetime)
	is_updated_later_than(datetime)
	get_custom_attributes(): str
	get_custom_attributes_as_dict(): dict
	get_custom_attributes_names(): set[]
	get_custom_attributes_values(): list[]

t_thin_dto(base_dto)
	+id, uid, is_active

t_write_dto(base_write_dto)
	{attributes}, custom_attributes
	get_uid()
	get_attr_one()
	...
	value_columns ?? custom_attributes = {}
	attributes ?? custom_attributes = {}
	value_attributes

t_read_dto(base_read_dto, t_thin_dto, t_write_dto)
	override attributes + metadata + FKs + custom_attributes
	get_model()
	get_
	get_as_long_description(): str
	get_row_comment(): str
	get_created_date()
	get_live_time_seconds(): float
	get_live_time_hours(): float
	get_last_updated_date()


t_full_dto
	attributes + custom_attributes + metadata + FKs + FK attributes

t_dtos(list[t_read_dto]) !!! TYPE t_dtos = list[t_read_dto]
	get_rows(): list[t_read_dto]
	get_uids(): list[string]
	get_ids(): list[int]
	get_names(): list[str]
	get(col_name)
	order_by_id():
	order_by_uid():
	order_by_created():
	order_by_updated():
	filter_active(): list[t_read_dto]
	filter_inactive(): list[t_read_dto]



DAOs
	base_dao
	base_read_dao -- only read methods, no update, insert, delete
	base_write_dao
	execute()

t_dao
	get_count_all()
	get_count_active()
	get_count_inactive()
	get_count_by_column(col_name, col_value)
	get_count_by_column_values(col_name, col_values: list[any])

	group_by_col(col_name): groupped_dto(column_value, rows_count, created_date_min, created_date_max...)
	select col_name, count(*) as rows_count, min(), max() as created_date_max from t group by col_name order by col_name

	get_rows_all(n=1000): list[t_read_dto]
	select * frm t limit n
	get_rows_active(n=1000): list[t_read_dto
	select * from t where is_active=1 limit n
	get_rows_inactive(n=1000): list[t_read_dto]
	select * from t where is_active=0 limit n

	get_by_uid_active(uid): Option[t_read_dto]
	select * from t where is_active=1 and t_uid=? limit 1
	get_by_id_active(id):
	select * from t where is_active=1 and id=? limit 1
	get_by_uid_or_none_active(): t_read_dto | None
	select * from t where is_active=1 and uid=? limit 1
	get_latest_created_active(n): list[t_read_dto]
	select * from t where is_active=1 order by created_date desc limit n
	get_latest_created_all(n): list[t_read_dto]
	select * from t order by created_date desc limit n
	get_latest_removed(n): list[t_read_dto]
	select * from t where is_active=0 order by removed_date desc limit n

	get_latest_updated(n): list[t_read_dto]
	select * from t order by created_date desc limit n
	get_by_query(sql): list[t_read_dto]
	sql
	get_by_column(col_name, col_value, n): list[t_read_dto]
	select * from t where col_name=? limit n
	get_all_uids(n): list[t_read_dto]

	get_active_: list[t_read_dto]
	get_column(col_name, )

	add_single(t_write_dto):
	add_and_get_single(t_write_dto): t_read_dto
	add_many(list[t_write_dto]) -> int
	add_or_update(list[t_write_dto], updated_by: str)


	update_touch(updated_by: str)
	update t set last_updated_date=now(), row_version=row_version+1, updated_by=?
	update_by_uid(t_write_dto, updated_by: str):
	update_by_condition(sql) ????
	update_comment(uid, comment)


	delete_logically_by_uid(uid): int
	delete_logically_by_name(name): int
	delete_logically_by_condition(sql): int
	delete_by

	FOR EACH FK:
	get_by_fk1(uid)


--








;            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Afghanistan', 'AF', 'AFG', '004', '93', 'AFN', 'Kabul', 'Asia', 'Southern Asia', '142', '33', '65', 'Afghanistan Afghani', '37100000', 'Balochi,Dari,Pashto,Turkmenian,Uzbek', '652000', '-', '.af');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Aland Islands', 'AX', 'ALA', '248', '-', '-', '-', 'Europe', 'Northern Europe', '150', '-', '-', '-', '-', '-', '-', '-', '.ax');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Albania', 'AL', 'ALB', '008', '355', 'ALL', 'Tirana', 'Europe', 'Southern Europe', '150', '41', '20', 'Albanian Lek', '2866000', 'Albaniana,Greek,Macedonian', '28000', '530', '.al');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Algeria', 'DZ', 'DZA', '012', '213', 'DZD', 'Alger', 'Africa', 'Northern Africa', '002', '28', '3', 'Algerian Dinar', '42200000', 'Arabic,Berberi', '2381000', '613', '.dz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'American Samoa', 'AS', 'ASM', '016', '1684', 'USD', 'Fagatogo', 'Oceania', 'Polynesia', '009', ' -14.3333', '-170', 'US Dollar', '55000', 'English,Samoan,Tongan', '199', '-', '.as');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Andorra', 'AD', 'AND', '020', '376', 'EUR', 'Andorra la Vella', 'Europe', 'Southern Europe', '150', ' 42.5', ' 1.6', 'Euro', '77000', 'Catalan,French,Portuguese,Spanish', '468', '-', '.ad');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Angola', 'AO', 'AGO', '024', '244', 'AOA', 'Luanda', 'Africa', 'Sub-Saharan Africa', '002', ' -12.5', ' 18.5', 'Angolan Kwanza', '30800000', 'Ambo,Chokwe,Kongo,Luchazi,Luimbe-nganguela,Luvale,Mbundu,Nyaneka-nkhumbi,Ovimbundu', '1246000', '-', '.ao');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Anguilla', 'AI', 'AIA', '660', '1264', 'XCD', 'The Valley', 'Americas', 'Latin America and the Caribbean', '019', ' 18.25', ' -63.1667', 'East Caribbean Dollar', '15000', 'English', '96', '-', '.ai');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Antarctica', '', 'Antarctica', 'AQ', 'ATA', '010', '672', 'XCD', 'null ', '', '', '', '-90', '0', 'East Caribbean Dollar', '1000', '-', '13100000', '-', '.aq');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Antigua and Barbuda', 'AG', 'ATG', '028', '1268', 'XCD', 'Saint Johns', 'Americas', 'Latin America and the Caribbean', '019', ' 17.05', ' -61.8', 'East Caribbean Dollar', '96000', 'Creole English,English', '442', '-', '.ag');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Argentina', 'AR', 'ARG', '032', '54', 'ARS', 'Buenos Aires', 'Americas', 'Latin America and the Caribbean', '019', '-34', '-64', 'Argentine Peso', '44400000', 'Indian Languages,Italian,Spanish', '2780000', '778 – 779', '.ar');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Armenia', 'AM', 'ARM', '051', '374', 'AMD', 'Yerevan', 'Asia', 'Western Asia', '142', '40', '45', 'Armenian Dram', '2951000', 'Armenian,Azerbaijani', '29000', '485', '.am');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Aruba', 'AW', 'ABW', '533', '297', 'AWG', 'Oranjestad', 'Americas', 'Latin America and the Caribbean', '019', ' 12.5', ' -69.9667', 'Aruban Guilder', '105000', 'Dutch,English,Papiamento,Spanish', '193', '-', '.aw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Australia', 'AU', 'AUS', '036', '61', 'AUD', 'Canberra', 'Oceania', 'Australia and New Zealand', '009', '-27', '133', 'Australian Dollar', '24900000', 'Arabic,Canton Chinese,English,German,Greek,Italian,Serbo-Croatian,Vietnamese', '7741000', '930 – 939', '.au');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Austria', 'AT', 'AUT', '040', '43', 'EUR', 'Wien', 'Europe', 'Western Europe', '150', ' 47.3333', ' 13.3333', 'Euro', '8840000', 'Czech,German,Hungarian,Polish,Romanian,Serbo-Croatian,Slovene,Turkish', '83000', '900 – 919', '.at');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Azerbaijan', 'AZ', 'AZE', '031', '994', 'AZN', 'Baku', 'Asia', 'Western Asia', '142', ' 40.5', ' 47.5', 'Azerbaijan New Manat', '9939000', 'Armenian,Azerbaijani,Lezgian,Russian', '86000', '476', '.az');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Bahamas', 'BS', 'BHS', '044', '1242', 'BSD', 'Nassau', 'Americas', 'Latin America and the Caribbean', '019', ' 24.25', '-76', 'Bahamian Dollar', '385000', 'Creole English,Creole French', '13000', '-', '.bs');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Bahrain', 'BH', 'BHR', '048', '973', 'BHD', 'al-Manama', 'Asia', 'Western Asia', '142', '26', ' 50.55', 'Bahraini Dinar', '1569000', 'Arabic,English', '694', '608', '.bh');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Bangladesh', 'BD', 'BGD', '050', '880', 'BDT', 'Dhaka', 'Asia', 'Southern Asia', '142', '24', '90', 'Bangladeshi Taka', '161300000', 'Bengali,Chakma,Garo,Khasi,Marma,Santhali,Tripuri', '143000', '-', '.bd');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Barbados', 'BB', 'BRB', '052', '1246', 'BBD', 'Bridgetown', 'Americas', 'Latin America and the Caribbean', '019', ' 13.1667', ' -59.5333', 'Barbados Dollar', '286000', 'Bajan,English', '430', '-', '.bb');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Belarus', 'BY', 'BLR', '112', '375', 'BYR', 'Minsk', 'Europe', 'Eastern Europe', '150', '53', '28', 'Belarussian Ruble', '9483000', 'Belorussian,Polish,Russian,Ukrainian', '207000', '481', '.by');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Belgium', 'BE', 'BEL', '056', '32', 'EUR', 'Bruxelles [Brussel]', 'Europe', 'Western Europe', '150', ' 50.8333', '4', 'Euro', '11400000', 'Arabic,Dutch,French,German,Italian,Turkish', '30000', '-', '.be');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Belize', 'BZ', 'BLZ', '084', '501', 'BZD', 'Belmopan', 'Americas', 'Latin America and the Caribbean', '019', ' 17.25', ' -88.75', 'Belize Dollar', '383000', 'English,Garifuna,Maya Languages,Spanish', '22000', '-', '.bz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Benin', 'BJ', 'BEN', '204', '229', 'XOF', 'Porto-Novo', 'Africa', 'Sub-Saharan Africa', '002', ' 9.5', ' 2.25', 'CFA Franc BCEAO', '11400000', 'Adja,Aizo,Bariba,Fon,Ful,Joruba,Somba', '112000', '-', '.bj');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Bermuda', 'BM', 'BMU', '060', '1441', 'BMD', 'Hamilton', 'Americas', 'Northern America', '019', ' 32.3333', ' -64.75', 'Bermudian Dollar', '63000', 'English', '53', '-', '.bm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Bhutan', 'BT', 'BTN', '064', '975', 'BTN', 'Thimphu', 'Asia', 'Southern Asia', '142', ' 27.5', ' 90.5', 'Bhutan Ngultrum', '754000', 'Asami,Dzongkha,Nepali', '47000', '-', '.bt');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Bolivia', 'BO', 'BOL', '068', '591', 'BOB', 'La Paz', 'Americas', 'Latin America and the Caribbean', '019', '-17', '-65', 'Boliviano', '11300000', 'Aimar√°,Guaran√≠,Ket¬öua,Spanish', '1098000', '777', '.bo');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Bonaire, Sint Eustatius and Saba', 'BQ', 'BES', '535', '-', '-', '-', 'Americas', 'Latin America and the Caribbean', '019', '-', '-', '-', '-', '-', '-', '-', '.bq');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Bosnia and Herzegovina', 'BA', 'BIH', '070', '387', 'BAM', 'Sarajevo', 'Europe', 'Southern Europe', '150', '44', '18', '-', '3323000', 'Bosnian', '51000', '387', '.ba');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Botswana', 'BW', 'BWA', '072', '267', 'BWP', 'Gaborone', 'Africa', 'Sub-Saharan Africa', '002', '-22', '24', 'Botswana Pula', '2254000', 'Khoekhoe,Ndebele,San,Shona,Tswana', '581000', '-', '.bw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Antarctica', '', 'Bouvet Island', 'BV', 'BVT', '074', '55', 'NOK', 'null ', 'Americas', 'Latin America and the Caribbean', '019', ' -54.4333', ' 3.4', 'Norwegian Krone', '0', '-', '59', '-', '.no');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Brazil', 'BR', 'BRA', '076', '55', 'BRL', 'Brasília', 'Americas', 'Latin America and the Caribbean', '019', '-10', '-55', 'Brazilian Real', '209400000', 'German,Indian Languages,Italian,Japanese,Portuguese', '8547000', '789 – 790', '.br');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'British Indian Ocean Territory', 'IO', 'IOT', '086', '246', 'USD', 'null ', 'Africa', 'Sub-Saharan Africa', '002', '-6', ' 71.5', 'US Dollar', '0', '-', '78', '-', '.io');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Brunei', 'BN', 'BRN', '096', '673', 'BND', 'Bandar Seri Begawan', 'Asia', 'South-eastern Asia', '142', ' 4.5', ' 114.6667', '0', '428000', 'Chinese,English,Malay,Malay-English', '5765', '623', '.bn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Bulgaria', 'BG', 'BGR', '100', '359', 'BGN', 'Sofia', 'Europe', 'Eastern Europe', '150', '43', '25', 'Bulgarian Lev', '7025000', 'Bulgariana,Macedonian,Romani,Turkish', '110000', '380', '.bg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Burkina Faso', 'BF', 'BFA', '854', '226', 'XOF', 'Ouagadougou', 'Africa', 'Sub-Saharan Africa', '002', '13', '-2', 'CFA Franc BCEAO', '19700000', 'Busansi,Dagara,Dyula,Ful,Gurma,Mossi', '274000', '-', '.bf');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Burundi', 'BI', 'BDI', '108', '257', 'BIF', 'Bujumbura', 'Africa', 'Sub-Saharan Africa', '002', ' -3.5', '30', 'Burundi Franc', '11100000', 'French,Kirundi,Swahili', '27000', '-', '.bi');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Cape Verde', 'CV', 'CPV', '132', '238', 'CVE', 'Praia', 'Africa', 'Sub-Saharan Africa', '002', '16', '-24', 'Cape Verde Escudo', '543000', 'Crioulo,Portuguese', '4033', '-', '.cv');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Cambodia', 'KH', 'KHM', '116', '855', 'KHR', 'Phnom Penh', 'Asia', 'South-eastern Asia', '142', '13', '105', 'Kampuchean Riel', '16200000', 'Chinese,Khmer,T¬öam,Vietnamese', '181000', '884', '.kh');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Cameroon', 'CM', 'CMR', '120', '237', 'XAF', 'Yaound', 'Africa', 'Sub-Saharan Africa', '002', '6', '12', 'CFA Franc BEAC', '25200000', 'Bamileke-bamum,Duala,Fang,Ful,Maka,Mandara,Masana,Tikar', '475000', '-', '.cm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Canada', 'CA', 'CAN', '124', '1', 'CAD', 'Ottawa', 'Americas', 'Northern America', '019', '60', '-95', 'Canadian Dollar', '37000000', 'Chinese,Dutch,English,Eskimo Languages,French,German,Italian,Polish,Portuguese,Punjabi,Spanish,Ukrainian', '9970000', '000 – 019', '.ca');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Cayman Islands', 'KY', 'CYM', '136', '1345', 'KYD', 'George Town', 'Americas', 'Latin America and the Caribbean', '019', ' 19.5', ' -80.5', 'Cayman Islands Dollar', '64000', 'English', '264', '-', '.ky');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Central African Republic', 'CF', 'CAF', '140', '236', 'XAF', 'Bangui', 'Africa', 'Sub-Saharan Africa', '002', '7', '21', 'CFA Franc BEAC', '4666000', 'Banda,Gbaya,Mandjia,Mbum,Ngbaka,Sara', '622000', '-', '.cf');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Chad', 'TD', 'TCD', '148', '235', 'XAF', 'NDjam', 'Africa', 'Sub-Saharan Africa', '002', '15', '19', '0', '15400000', 'Arabic,Gorane,Hadjarai,Kanem-bornu,Mayo-kebbi,Ouaddai,Sara,Tandjile', '1284000', '-', '.td');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Chile', 'CL', 'CHL', '152', '56', 'CLP', 'Santiago de Chile', 'Americas', 'Latin America and the Caribbean', '019', '-30', '-71', 'Chilean Peso', '18700000', 'Aimar√°,Araucan,Rapa nui,Spanish', '756000', '780', '.cl');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'China', 'CN', 'CHN', '156', '86', 'CNY', 'Peking', 'Asia', 'Eastern Asia', '142', '35', '105', 'Yuan Renminbi', '1392700000', 'Chinese,Dong,Hui,Mant¬öu,Miao,Mongolian,Puyi,Tibetan,Tujia,Uighur,Yi,Zhuang', '9572000', '690 – 699', '.cn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Christmas Island', 'CX', 'CXR', '162', '61', 'AUD', 'Flying Fish Cove', 'Oceania', 'Australia and New Zealand', '009', ' -10.5', ' 105.6667', 'Australian Dollar', '1000', 'Chinese,English', '135', '-', '.cx');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Cocos (Keeling) Islands', 'CC', 'CCK', '166', '61', 'AUD', 'West Island', 'Oceania', 'Australia and New Zealand', '009', ' -12.5', ' 96.8333', ' Australian Dollar', '0', 'English,Malay', '14', '-', '.cc');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Colombia', 'CO', 'COL', '170', '57', 'COP', 'Santaf', 'Americas', 'Latin America and the Caribbean', '019', '4', '-72', 'Colombian Peso', '49600000', 'Arawakan,Caribbean,Chibcha,Creole English,Spanish', '1138000', '770 – 771', '.co');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Comoros', 'KM', 'COM', '174', '269', 'KMF', 'Moroni', 'Africa', 'Sub-Saharan Africa', '002', ' -12.1667', ' 44.25', 'Comoros Franc', '832000', 'Comorian,Comorian-Arabic,Comorian-French,Comorian-madagassi,Comorian-Swahili', '1862', '-', '.km');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Congo', 'CG', 'COG', '178', '242', 'XAF', 'Brazzaville', 'Africa', 'Sub-Saharan Africa', '002', '-1', '15', 'CFA Franc BEAC', '5244000', 'Kongo,Mbete,Mboshi,Punu,Sango,Teke', '342000', '-', '.cg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'The Democratic Republic of Congo', 'CD', 'COD', '180', '243', 'CDF', 'Kinshasa', 'Africa', 'Sub-Saharan Africa', '002', '-', '-', 'Franc Congolais', '84000000', '-', '-', '-', '.cd');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Cook Islands', 'CK', 'COK', '184', '682', 'NZD', 'Avarua', 'Oceania', 'Polynesia', '009', ' -21.2333', ' -159.7667', 'New Zealand Dollar', '17000', 'English,Maori', '236', '-', '.ck');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Costa Rica', 'CR', 'CRI', '188', '506', 'CRC', 'San Jos', 'Americas', 'Latin America and the Caribbean', '019', '10', '-84', 'Costa Rican Colon', '4999000', 'Chibcha,Chinese,Creole English,Spanish', '51000', '744', '.cr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Cote dIvoire', 'CI', 'CIV', '384', '-', '-', '-', 'Africa', 'Sub-Saharan Africa', '002', '-', '-', '-', '-', '-', '-', '-', '.ci');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Croatia', 'HR', 'HRV', '191', '385', 'HRK', 'Zagreb', 'Europe', 'Southern Europe', '150', ' 45.1667', ' 15.5', 'Croatian Kuna', '4087000', 'Serbo-Croatian,Slovene', '56000', '385', '.hr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Cuba', 'CU', 'CUB', '192', '53', 'CUP', 'La Habana', 'Americas', 'Latin America and the Caribbean', '019', ' 21.5', '-80', 'Cuban Peso', '11300000', 'Spanish', '110000', '850', '.cu');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Curasao', 'CW', 'CUW', '531', '-', '-', '-', 'Americas', 'Latin America and the Caribbean', '019', '-', '-', '-', '-', '-', '-', '-', '.cw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Cyprus', 'CY', 'CYP', '196', '357', 'EUR', 'Nicosia', 'Asia', 'Western Asia', '142', '35', '33', 'Euro', '1189000', 'Greek,Turkish', '9251', '529', '.cy');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Czech Republic', 'CZ', 'CZE', '203', '420', 'CZK', 'Praha', 'Europe', 'Eastern Europe', '150', ' 49.75', ' 15.5', '0', '10600000', 'Czech,German,Hungarian,Moravian,Polish,Romani,Silesiana,Slovak', '78000', '859', '.cz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Denmark', 'DK', 'DNK', '208', '45', 'DKK', 'Copenhagen', 'Europe', 'Northern Europe', '150', '56', '10', 'Danish Krone', '5793000', 'Arabic,Danish,English,German,Norwegian,Swedish,Turkish', '43000', '570 – 579', '.dk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Djibouti', 'DJ', 'DJI', '262', '253', 'DJF', 'Djibouti', 'Africa', 'Sub-Saharan Africa', '002', ' 11.5', '43', 'Djibouti Franc', '958000', 'Afar,Arabic,Somali', '23000', '-', '.dj');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Dominica', 'DM', 'DMA', '212', '1767', 'XCD', 'Roseau', 'Americas', 'Latin America and the Caribbean', '019', ' 15.4167', ' -61.3333', 'East Caribbean Dollar', '71000', 'Creole English,Creole French', '751', '-', '.dm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Dominican Republic', 'DO', 'DOM', '214', '1849', 'DOP', 'Santo Domingo de Guzm', 'Americas', 'Latin America and the Caribbean', '019', '19', ' -70.6667', 'Dominican Peso', '10600000', 'Creole French,Spanish', '48000', '746', '.do');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Ecuador', 'EC', 'ECU', '218', '593', 'ECS', 'Quito', 'Americas', 'Latin America and the Caribbean', '019', '-2', ' -77.5', 'Ecuador Sucre', '17000000', 'Ket¬öua,Spanish', '283000', '786', '.ec');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Egypt', 'EG', 'EGY', '818', '20', 'EGP', 'Cairo', 'Africa', 'Northern Africa', '002', '27', '30', 'Egyptian Pound', '98400000', 'Arabic,Sinaberberi', '1001000', '622', '.eg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'El Salvador', 'SV', 'SLV', '222', '503', 'SVC', 'San Salvador', 'Americas', 'Latin America and the Caribbean', '019', ' 13.8333', ' -88.9167', 'El Salvador Colon', '6420000', 'Nahua,Spanish', '21000', '741', '.sv');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Equatorial Guinea', 'GQ', 'GNQ', '226', '240', 'XAF', 'Malabo', 'Africa', 'Sub-Saharan Africa', '002', '2', '10', 'CFA Franc BEAC', '1308000', 'Bubi,Fang', '28000', '-', '.gq');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Eritrea', 'ER', 'ERI', '232', '291', 'ERN', 'Asmara', 'Africa', 'Sub-Saharan Africa', '002', '15', '39', 'Eritrean Nakfa', '6213000', 'Afar,Bilin,Hadareb,Saho,Tigre,Tigrigna', '117000', '-', '.er');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Estonia', 'EE', 'EST', '233', '372', 'EUR', 'Tallinn', 'Europe', 'Northern Europe', '150', '59', '26', 'Euro', '1321000', 'Belorussian,Estonian,Finnish,Russian,Ukrainian', '45000', '474', '.ee');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Eswatini', 'SZ', 'SWZ', '748', '-', '-', '-', 'Africa', 'Sub-Saharan Africa', '002', '-', '-', '-', '-', '-', '-', '-', '.sz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Ethiopia', 'ET', 'ETH', '231', '251', 'ETB', 'Addis Abeba', 'Africa', 'Sub-Saharan Africa', '002', '8', '38', 'Ethiopian Birr', '109200000', 'Amharic,Gurage,Oromo,Sidamo,Somali,Tigrigna,Walaita', '1104000', '-', '.et');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Falkland Islands', 'FK', 'FLK', '238', '500', 'FKP', 'Stanley', 'Americas', 'Latin America and the Caribbean', '019', '-', '-', '0', '2000', 'English', '12000', '-', '.fk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Faroe Islands', 'FO', 'FRO', '234', '298', 'DKK', 'Tórshavn', 'Europe', 'Northern Europe', '150', '62', '-7', ' Danish Krone', '48000', 'Danish,Faroese', '1399', '570 – 579', '.fo');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Fiji Islands', 'FJ', 'FJI', '242', '679', 'FJD', 'Suva', 'Oceania', 'Melanesia', '009', '-', '-', '0', '883000', 'Fijian,Hindi', '18000', '-', '.fj');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Finland', 'FI', 'FIN', '246', '358', 'EUR', 'Helsinki [Helsingfors]', 'Europe', 'Northern Europe', '150', '64', '26', 'Euro', '5515000', 'Estonian,Finnish,Russian,Saame,Swedish', '338000', '640 – 649', '.fi');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'France', 'FR', 'FRA', '250', '33', 'EUR', 'Paris', 'Europe', 'Western Europe', '150', '46', '2', 'Euro', '66900000', 'Arabic,French,Italian,Portuguese,Spanish,Turkish', '551000', '-', '.fr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'French Guiana', 'GF', 'GUF', '254', '594', 'EUR', 'Cayenne', 'Americas', 'Latin America and the Caribbean', '019', '4', '-53', 'Euro', '290000', 'Creole French,Indian Languages', '90000', '-', '.gf');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'French Polynesia', 'PF', 'PYF', '258', '689', 'XPF', 'Papeete', 'Oceania', 'Polynesia', '009', '-15', '-140', '0', '277000', 'Chinese,French,Tahitian', '4000', '-', '.pf');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Antarctica', '', 'French Southern Territories', 'TF', 'ATF', '260', '262', 'EUR', 'null ', 'Africa', 'Sub-Saharan Africa', '002', '-43', '67', 'Euro', '0', '-', '7780', '-', '.tf');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Gabon', 'GA', 'GAB', '266', '241', 'XAF', 'Libreville', 'Africa', 'Sub-Saharan Africa', '002', '-1', ' 11.75', 'CFA Franc BEAC', '2119000', 'Fang,Mbete,Mpongwe,Punu-sira-nzebi', '267000', '-', '.ga');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Gambia', 'GM', 'GMB', '270', '220', 'GMD', 'Banjul', 'Africa', 'Sub-Saharan Africa', '002', ' 13.4667', ' -16.5667', 'Gambian Dalasi', '2280000', 'Diola,Ful,Malinke,Soninke,Wolof', '11000', '-', '.gm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Georgia', 'GE', 'GEO', '268', '995', 'GEL', 'Tbilisi', 'Asia', 'Western Asia', '142', '42', ' 43.5', 'Georgian Lari', '3726000', 'Abhyasi,Armenian,Azerbaijani,Georgiana,Osseetti,Russian', '69000', '486', '.ge');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Germany', 'DE', 'DEU', '276', '49', 'EUR', 'Berlin', 'Europe', 'Western Europe', '150', '51', '9', 'Euro', '82900000', 'German,Greek,Italian,Polish,Southern Slavic Languages,Turkish', '357000', '400 – 440', '.de');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Ghana', 'GH', 'GHA', '288', '233', 'GHS', 'Accra', 'Africa', 'Sub-Saharan Africa', '002', '8', '-2', 'Ghanaian Cedi', '29700000', 'Akan,Ewe,Ga-adangme,Gurma,Joruba,Mossi', '238000', '603', '.gh');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Gibraltar', 'GI', 'GIB', '292', '350', 'GIP', 'Gibraltar', 'Europe', 'Southern Europe', '150', ' 36.1833', ' -5.3667', 'Gibraltar Pound', '33000', 'Arabic,English', '6', '-', '.gi');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Greece', 'GR', 'GRC', '300', '30', 'EUR', 'Athenai', 'Europe', 'Southern Europe', '150', '39', '22', 'Euro', '10700000', 'Greek,Turkish', '131000', '520 – 521', '.gr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Greenland', 'GL', 'GRL', '304', '299', 'DKK', 'Nuuk', 'Americas', 'Northern America', '019', '72', '-40', 'Danish Krone', '56000', 'Danish,Greenlandic', '2166000', '570 – 579', '.gl');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Grenada', 'GD', 'GRD', '308', '1473', 'XCD', 'Saint Georges', 'Americas', 'Latin America and the Caribbean', '019', ' 12.1167', ' -61.6667', 'East Carribean Dollar', '111000', 'Creole English', '344', '-', '.gd');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Guadeloupe', 'GP', 'GLP', '312', '590', 'EUR', 'Basse-Terre', 'Americas', 'Latin America and the Caribbean', '019', ' 16.25', ' -61.5833', '0', '395000', 'Creole French,French', '1705', '-', '.gp');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Guam', 'GU', 'GUM', '316', '1671', 'USD', 'Aga', 'Oceania', 'Micronesia', '009', ' 13.4667', ' 144.7833', '0', '165000', 'Chamorro,English,Japanese,Korean,Philippene Languages', '549', '-', '.gu');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Guatemala', 'GT', 'GTM', '320', '502', 'QTQ', 'Ciudad de Guatemala', 'Americas', 'Latin America and the Caribbean', '019', ' 15.5', ' -90.25', 'Guatemalan Quetzal', '17200000', 'Cakchiquel,Kekch√≠,Mam,Quich√©,Spanish', '108000', '740', '.gt');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Guernsey', 'GG', 'GGY', '831', '-', '-', '-', 'Europe', 'Northern Europe', '150', ' 49.5', ' -2.56', '-', '-', '-', '-', '-', '.gg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Guinea', 'GN', 'GIN', '324', '224', 'GNF', 'Conakry', 'Africa', 'Sub-Saharan Africa', '002', '11', '-10', 'Guinea Franc', '12400000', 'Ful,Kissi,Kpelle,Loma,Malinke,Susu,Yalunka', '245000', '-', '.gn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Guinea-Bissau', 'GW', 'GNB', '624', '245', 'CFA', 'Bissau', 'Africa', 'Sub-Saharan Africa', '002', '12', '-15', '0', '1874000', 'Balante,Crioulo,Ful,Malinke,Mandyako,Portuguese', '36000', '-', '.gw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Guyana', 'GY', 'GUY', '328', '592', 'GYD', 'Georgetown', 'Americas', 'Latin America and the Caribbean', '019', '5', '-59', 'Guyana Dollar', '779000', 'Arawakan,Caribbean,Creole English', '214000', '-', '.gy');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Haiti', 'HT', 'HTI', '332', '509', 'HTG', 'Port-au-Prince', 'Americas', 'Latin America and the Caribbean', '019', '19', ' -72.4167', 'Haitian Gourde', '11100000', 'French,Haiti Creole', '27000', '-', '.ht');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Antarctica', '', 'Heard Island and McDonald Islands', 'HM', 'HMD', '334', '672', 'AUD', '0', 'Oceania', 'Australia and New Zealand', '009', ' -53.1', ' 72.5167', 'Australian Dollar', '0', '-', '359', '-', '.hm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Holy See', 'VA', 'VAT', '336', '379', '-', 'Citt', 'Europe', 'Southern Europe', '150', '-', '-', '0', '0', '-', '-', '-', '.va');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Honduras', 'HN', 'HND', '340', '504', 'HNL', 'Tegucigalpa', 'Americas', 'Latin America and the Caribbean', '019', '15', ' -86.5', 'Honduran Lempira', '9587000', 'Creole English,Garifuna,Miskito,Spanish', '112000', '742', '.hn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Hong Kong', 'HK', 'HKG', '344', '852', 'HKD', 'Victoria', 'Asia', 'Eastern Asia', '142', ' 22.25', ' 114.1667', 'Hong Kong Dollar', '7451000', 'Canton Chinese,Chiu chau,English,Fukien,Hakka', '1075', '489', '.hk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Hungary', 'HU', 'HUN', '348', '36', 'HUF', 'Budapest', 'Europe', 'Eastern Europe', '150', '47', '20', 'Hungarian Forint', '9775000', 'German,Hungarian,Romani,Romanian,Serbo-Croatian,Slovak', '93000', '599', '.hu');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Iceland', 'IS', 'ISL', '352', '354', 'ISK', 'Reykjav', 'Europe', 'Northern Europe', '150', '65', '-18', 'Iceland Krona', '352000', 'English,Icelandic', '103000', '569', '.is');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'India', 'IN', 'IND', '356', '91', 'INR', 'New Delhi', 'Asia', 'Southern Asia', '142', '20', '77', 'Indian Rupee', '1352600000', 'Asami,Bengali,Gujarati,Hindi,Kannada,Malayalam,Marathi,Odia,Punjabi,Tamil,Telugu,Urdu,Sanskrit,English,Konkani,Nepali,Bodo,Kashmiri,Maithili,Santali,Sindhi', '3287000', '890', '.in');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Indonesia', 'ID', 'IDN', '360', '62', 'IDR', 'Jakarta', 'Asia', 'South-eastern Asia', '142', '-5', '120', 'Indonesian Rupiah', '267600000', 'Bahasa,Bali,Banja,Batakki,Bugi,Javanese,Madura,Malay,Minangkabau,Sunda', '1904000', '899', '.id');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Iran', 'IR', 'IRN', '364', '98', 'IRR', 'Tehran', 'Asia', 'Southern Asia', '142', '-', '-', 'Iranian Rial', '81800000', 'Arabic,Azerbaijani,Bakhtyari,Balochi,Gilaki,Kurdish,Luri,Mazandarani,Persian,Turkmenian', '1648000', '626', '.ir');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Iraq', 'IQ', 'IRQ', '368', '964', 'IQD', 'Baghdad', 'Asia', 'Western Asia', '142', '33', '44', 'Iraqi Dinar', '38400000', 'Arabic,Assyrian,Azerbaijani,Kurdish,Persian', '438000', '-', '.iq');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Ireland', 'IE', 'IRL', '372', '353', 'EUR', 'Dublin', 'Europe', 'Northern Europe', '150', '53', '-8', 'Euro', '4867000', 'English,Irish', '70000', '-', '.ie');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Isle of Man', 'IM', 'IMN', '833', '-', '-', '-', 'Europe', 'Northern Europe', '150', ' 54.23', ' -4.55', '-', '-', '-', '-', '-', '.im');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Israel', 'IL', 'ISR', '376', '972', 'ILS', 'Jerusalem', 'Asia', 'Western Asia', '142', ' 31.5', ' 34.75', 'Israeli New Shekel', '8882000', 'Arabic,Hebrew,Russian', '21000', '729', '.il');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Italy', 'IT', 'ITA', '380', '39', 'EUR', 'Roma', 'Europe', 'Southern Europe', '150', ' 42.8333', ' 12.8333', 'Euro', '60400000', 'Albaniana,French,Friuli,German,Italian,Romani,Sardinian,Slovene', '301000', '-', '.it');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Jamaica', 'JM', 'JAM', '388', '1876', 'JMD', 'Kingston', 'Americas', 'Latin America and the Caribbean', '019', ' 18.25', ' -77.5', 'Jamaican Dollar', '2934000', 'Creole English,Hindi', '10000', '-', '.jm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Japan', 'JP', 'JPN', '392', '81', 'JPY', 'Tokyo', 'Asia', 'Eastern Asia', '142', '36', '138', 'Japanese Yen', '126500000', 'Ainu,Chinese,English,Japanese,Korean,Philippene Languages', '377000', '450 – 459', '.jp');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Jersey', 'JE', 'JEY', '832', '-', '-', '-', 'Europe', 'Northern Europe', '150', ' 49.21', ' -2.13', '-', '-', '-', '-', '-', '.je');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Jordan', 'JO', 'JOR', '400', '962', 'JOD', 'Amman', 'Asia', 'Western Asia', '142', '31', '36', 'Jordanian Dinar', '9956000', 'Arabic,Armenian,Circassian', '88000', '625', '.jo');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Kazakhstan', 'KZ', 'KAZ', '398', '7', 'KZT', 'Astana', 'Asia', 'Central Asia', '142', '48', '68', '0', '18200000', 'German,Kazakh,Russian,Tatar,Ukrainian,Uzbek', '2724000', '-', '.kz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Kenya', 'KE', 'KEN', '404', '254', 'KES', 'Nairobi', 'Africa', 'Sub-Saharan Africa', '002', '1', '38', 'Kenyan Shilling', '51300000', 'Gusii,Kalenjin,Kamba,Kikuyu,Luhya,Luo,Masai,Meru,Nyika,Turkana', '580000', '616', '.ke');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Kiribati', 'KI', 'KIR', '296', '686', 'AUD', 'Bairiki', 'Oceania', 'Micronesia', '009', ' 1.4167', '173', 'Australian Dollar', '115000', 'Kiribati,Tuvalu', '726', '-', '.ki');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'North Korea', 'KP', 'PRK', '408', '850', 'KPW', 'Pyongyang', 'Asia', 'Eastern Asia', '142', '-', '-', 'North Korean Won', '25500000', 'Chinese,Korean', '120000', '867', '.kp');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'South Korea', 'KR', 'KOR', '410', '82', 'KRW', 'Seoul', 'Asia', 'Eastern Asia', '142', '37', ' 127.5', 'Korean Won', '51600000', 'Chinese,Korean', '99000', '880', '.kr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Kuwait', 'KW', 'KWT', '414', '965', 'KWD', 'Kuwait', 'Asia', 'Western Asia', '142', ' 29.3375', ' 47.6581', 'Kuwaiti Dinar', '4137000', 'Arabic,English', '17000', '627', '.kw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Kyrgyzstan', 'KG', 'KGZ', '417', '996', 'KGS', 'Bishkek', 'Asia', 'Central Asia', '142', '41', '75', 'Som', '6322000', 'Kazakh,Kirgiz,Russian,Tadzhik,Tatar,Ukrainian,Uzbek', '199000', '470', '.kg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Laos', 'LA', 'LAO', '418', '856', 'LAK', 'Vientiane', 'Asia', 'South-eastern Asia', '142', '-', '-', 'Lao Kip', '7061000', 'Lao,Lao-Soung,Mon-khmer,Thai', '236000', '-', '.la');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Latvia', 'LV', 'LVA', '428', '371', 'LVL', 'Riga', 'Europe', 'Northern Europe', '150', '57', '25', 'Latvian Lats', '1927000', 'Belorussian,Latvian,Lithuanian,Polish,Russian,Ukrainian', '64000', '475', '.lv');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Lebanon', 'LB', 'LBN', '422', '961', 'LBP', 'Beirut', 'Asia', 'Western Asia', '142', ' 33.8333', ' 35.8333', 'Lebanese Pound', '6848000', 'Arabic,Armenian,French', '10000', '528', '.lb');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Lesotho', 'LS', 'LSO', '426', '266', 'LSL', 'Maseru', 'Africa', 'Sub-Saharan Africa', '002', ' -29.5', ' 28.5', 'Lesotho Loti', '2108000', 'English,Sotho,Zulu', '30000', '-', '.ls');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Liberia', 'LR', 'LBR', '430', '231', 'LRD', 'Monrovia', 'Africa', 'Sub-Saharan Africa', '002', ' 6.5', ' -9.5', 'Liberian Dollar', '4818000', 'Bassa,Gio,Grebo,Kpelle,Kru,Loma,Malinke,Mano', '111000', '-', '.lr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Libyan Arab Jamahiriya', 'LY', 'LBY', '434', '218', 'LYD', 'Tripoli', 'Africa', 'Northern Africa', '002', '25', '17', '0', '6678000', 'Arabic,Berberi', '1759000', '-', '.ly');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Liechtenstein', 'LI', 'LIE', '438', '423', 'CHF', 'Vaduz', 'Europe', 'Western Europe', '150', ' 47.1667', ' 9.5333', 'Swiss Franc', '37000', 'German,Italian,Turkish', '160', '-', '.li');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Lithuania', 'LT', 'LTU', '440', '370', 'LTL', 'Vilnius', 'Europe', 'Northern Europe', '150', '56', '24', 'Lithuanian Litas', '2801000', 'Belorussian,Lithuanian,Polish,Russian,Ukrainian', '65000', '477', '.lt');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Luxembourg', 'LU', 'LUX', '442', '352', 'EUR', 'Luxembourg', 'Europe', 'Western Europe', '150', ' 49.75', ' 6.1667', 'Euro', '607000', 'French,German,Italian,Luxembourgish,Portuguese', '2586', '-', '.lu');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Macao', 'MO', 'MAC', '446', '853', 'MOP', 'Macao', 'Asia', 'Eastern Asia', '142', ' 22.1667', ' 113.55', '0', '631000', 'Canton Chinese,English,Mandarin Chinese,Portuguese', '18', '-', '.mo');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Madagascar', 'MG', 'MDG', '450', '261', 'MGF', 'Antananarivo', 'Africa', 'Sub-Saharan Africa', '002', '-20', '47', 'Malagasy Franc', '26200000', 'French,Malagasy', '587000', '-', '.mg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Malawi', 'MW', 'MWI', '454', '265', 'MWK', 'Lilongwe', 'Africa', 'Sub-Saharan Africa', '002', ' -13.5', '34', 'Malawi Kwacha', '18100000', 'Chichewa,Lomwe,Ngoni,Yao', '118000', '-', '.mw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Malaysia', 'MY', 'MYS', '458', '60', 'MYR', 'Kuala Lumpur', 'Asia', 'South-eastern Asia', '142', ' 2.5', ' 112.5', 'Malaysian Ringgit', '31500000', 'Chinese,Dusun,English,Iban,Malay,Tamil', '329000', '955', '.my');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Maldives', 'MV', 'MDV', '462', '960', 'MVR', 'Male', 'Asia', 'Southern Asia', '142', ' 3.25', '73', 'Maldive Rufiyaa', '515000', 'Dhivehi,English', '298', '-', '.mv');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Mali', 'ML', 'MLI', '466', '223', 'XOF', 'Bamako', 'Africa', 'Sub-Saharan Africa', '002', '17', '-4', 'CFA Franc BCEAO', '19000000', 'Bambara,Ful,Senufo and Minianka,Songhai,Soninke,Tamashek', '1240000', '-', '.ml');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Malta', 'MT', 'MLT', '470', '356', 'EUR', 'Valletta', 'Europe', 'Southern Europe', '150', ' 35.8333', ' 14.5833', 'Euro', '484000', 'English,Maltese', '316', '535', '.mt');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Marshall Islands', 'MH', 'MHL', '584', '692', 'USD', 'Dalap-Uliga-Darrit', 'Oceania', 'Micronesia', '009', '9', '168', 'US Dollar', '58000', 'English,Marshallese', '181', '-', '.mh');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Martinique', 'MQ', 'MTQ', '474', '596', 'EUR', 'Fort-de-France', 'Americas', 'Latin America and the Caribbean', '019', ' 14.6667', '-61', '0', '376000', 'Creole French,French', '1102', '-', '.mq');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Mauritania', 'MR', 'MRT', '478', '222', 'MRO', 'Nouakchott', 'Africa', 'Sub-Saharan Africa', '002', '20', '-12', 'Mauritanian Ouguiya', '4403000', 'Ful,Hassaniya,Soninke,Tukulor,Wolof,Zenaga', '1025000', '-', '.mr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Mauritius', 'MU', 'MUS', '480', '230', 'MUR', 'Port-Louis', 'Africa', 'Sub-Saharan Africa', '002', ' -20.2833', ' 57.55', 'Mauritius Rupee', '1265000', 'Bhojpuri,Creole French,French,Hindi,Marathi,Tamil', '2040', '609', '.mu');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Mayotte', 'YT', 'MYT', '175', '262', 'EUR', 'Mamoutzou', 'Africa', 'Sub-Saharan Africa', '002', ' -12.8333', ' 45.1667', 'Euro', '270000', 'French,Mahor√©,Malagasy', '373', '-', '.yt');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Mexico', 'MX', 'MEX', '484', '52', 'MXN', 'Ciudad de M', 'Americas', 'Latin America and the Caribbean', '019', '23', '-102', 'Mexican Nuevo Peso', '126100000', 'Mixtec,N√°huatl,Otom√≠,Spanish,Yucatec,Zapotec', '1958000', '750', '.mx');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Micronesia', 'FM', 'FSM', '583', '-', '-', '-', 'Oceania', 'Micronesia', '009', '-', '-', '-', '-', '-', '-', '-', '.fm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Moldova', 'MD', 'MDA', '498', '373', 'MDL', 'Chisinau', 'Europe', 'Eastern Europe', '150', '-', '-', 'Moldovan Leu', '2706000', 'Bulgariana,Gagauzi,Romanian,Russian,Ukrainian', '33000', '484', '.md');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Monaco', 'MC', 'MCO', '492', '377', 'EUR', 'Monaco-Ville', 'Europe', 'Western Europe', '150', ' 43.7333', ' 7.4', '0', '38000', 'English,French,Italian,Monegasque', '18000', '-', '.mc');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Mongolia', 'MN', 'MNG', '496', '976', 'MNT', 'Ulan Bator', 'Asia', 'Eastern Asia', '142', '46', '105', 'Mongolian Tugrik', '3170000', 'Bajad,Buryat,Dariganga,Dorbet,Kazakh,Mongolian', '1566000', '865', '.mn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Montenegro', 'ME', 'MNE', '499', '-', '-', 'Podgorica', 'Europe', 'Southern Europe', '150', '42', '19', '-', '631000', '-', '-', '-', '.me');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Montserrat', 'MS', 'MSR', '500', '1664', 'XCD', 'Plymouth', 'Americas', 'Latin America and the Caribbean', '019', ' 16.75', ' -62.2', 'East Caribbean Dollar', '5000', 'English', '102', '-', '.ms');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Morocco', 'MA', 'MAR', '504', '212', 'MAD', 'Rabat', 'Africa', 'Northern Africa', '002', '32', '-5', 'Moroccan Dirham', '36000000', 'Arabic,Berberi', '446000', '611', '.ma');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Mozambique', 'MZ', 'MOZ', '508', '258', 'MZN', 'Maputo', 'Africa', 'Sub-Saharan Africa', '002', ' -18.25', '35', 'Mozambique Metical', '29400000', 'Chuabo,Lomwe,Makua,Marendje,Nyanja,Ronga,Sena,Shona,Tsonga,Tswa', '801000', '-', '.mz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Myanmar', 'MM', 'MMR', '104', '95', 'MMR', 'Rangoon (Yangon)', 'Asia', 'South-eastern Asia', '142', '22', '98', 'Myanmar Kyat', '53700000', 'Burmese,Chin,Kachin,Karen,Kayah,Mon,Rakhine,Shan', '676000', '-', '.mm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Namibia', 'NA', 'NAM', '516', '264', 'NAD', 'Windhoek', 'Africa', 'Sub-Saharan Africa', '002', '-22', '17', 'Namibian Dollar', '2448000', 'Afrikaans,Caprivi,German,Herero,Kavango,Nama,Ovambo,San', '824000', '-', '.na');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Nauru', 'NR', 'NRU', '520', '674', 'AUD', 'Yaren', 'Oceania', 'Micronesia', '009', ' -0.5333', ' 166.9167', 'Australian Dollar', '12000', 'Chinese,English,Kiribati,Nauru,Tuvalu', '21', '-', '.nr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Nepal', 'NP', 'NPL', '524', '977', 'NPR', 'Kathmandu', 'Asia', 'Southern Asia', '142', '28', '84', 'Nepalese Rupee', '28000000', 'Bhojpuri,Hindi,Maithili,Nepali,Newari,Tamang,Tharu', '147000', '-', '.np');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Netherlands', 'NL', 'NLD', '528', '31', 'EUR', 'Amsterdam', 'Europe', 'Western Europe', '150', ' 52.5', ' 5.75', 'Euro', '17200000', 'Arabic,Dutch,Fries,Turkish', '41000', '870 – 879', '.nl');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'New Caledonia', 'NC', 'NCL', '540', '687', 'XPF', 'Noum', 'Oceania', 'Melanesia', '009', ' -21.5', ' 165.5', '0', '284000', 'French,Malenasian Languages,Polynesian Languages', '18000', '-', '.nc');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'New Zealand', 'NZ', 'NZL', '554', '64', 'NZD', 'Wellington', 'Oceania', 'Australia and New Zealand', '009', '-41', '174', 'New Zealand Dollar', '4841000', 'English,Maori', '270000', '940 – 949', '.nz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Nicaragua', 'NI', 'NIC', '558', '505', 'NIO', 'Managua', 'Americas', 'Latin America and the Caribbean', '019', '13', '-85', 'Nicaraguan Cordoba Oro', '6465000', 'Creole English,Miskito,Spanish,Sumo', '130000', '743', '.ni');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Niger', 'NE', 'NER', '562', '227', 'XOF', 'Niamey', 'Africa', 'Sub-Saharan Africa', '002', '16', '8', 'CFA Franc BCEAO', '22400000', 'Ful,Hausa,Kanuri,Songhai-zerma,Tamashek', '1267000', '-', '.ne');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Nigeria', 'NG', 'NGA', '566', '234', 'NGN', 'Abuja', 'Africa', 'Sub-Saharan Africa', '002', '10', '8', 'Nigerian Naira', '195800000', 'Bura,Edo,Ful,Hausa,Ibibio,Ibo,Ijo,Joruba,Kanuri,Tiv', '923000', '615', '.ng');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Niue', 'NU', 'NIU', '570', '683', 'NZD', 'Alofi', 'Oceania', 'Polynesia', '009', ' -19.0333', ' -169.8667', 'New Zealand Dollar', '1000', 'English,Niue', '260', '-', '.nu');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Norfolk Island', 'NF', 'NFK', '574', '672', 'AUD', 'Kingston', 'Oceania', 'Australia and New Zealand', '009', ' -29.0333', ' 167.95', 'Australian Dollar', '2000', 'English', '36', '-', '.nf');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'North Macedonia', 'MK', 'MKD', '807', '389', 'MKD', 'Skopje', 'Europe', 'Southern Europe', '150', '-', '-', 'Denar', '2084000', '-', '25000', '531', '.mk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Northern Mariana Islands', 'MP', 'MNP', '580', '1670', 'USD', 'Garapan', 'Oceania', 'Micronesia', '009', ' 15.2', ' 145.75', 'US Dollar', '56000', 'Carolinian,Chamorro,Chinese,English,Korean,Philippene Languages', '464', '-', '.mp');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Norway', 'NO', 'NOR', '578', '47', 'NOK', 'Oslo', 'Europe', 'Northern Europe', '150', '62', '10', 'Norwegian Krone', '5311000', 'Danish,English,Norwegian,Saame,Swedish', '323000', '700 – 709', '.no');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Oman', 'OM', 'OMN', '512', '968', 'OMR', 'Masqat', 'Asia', 'Western Asia', '142', '21', '57', 'Omani Rial', '4829000', 'Arabic,Balochi', '309000', '-', '.om');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Pakistan', 'PK', 'PAK', '586', '92', 'PKR', 'Islamabad', 'Asia', 'Southern Asia', '142', '30', '70', 'Pakistan Rupee', '212200000', 'Balochi,Brahui,Hindko,Pashto,Punjabi,Saraiki,Sindhi,Urdu', '796000', '896', '.pk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Palau', 'PW', 'PLW', '585', '680', 'USD', 'Koror', 'Oceania', 'Micronesia', '009', ' 7.5', ' 134.5', 'US Dollar', '17000', 'Chinese,English,Palau,Philippene Languages', '459', '-', '.pw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Palestine', 'PS', 'PSE', '275', '970', '-', 'Gaza', 'Asia', 'Western Asia', '142', '-', '-', '0', '4569000', 'Arabic,Hebrew', '6257', '-', '.ps');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Panama', 'PA', 'PAN', '591', '507', 'PAB', 'Ciudad de Panam', 'Americas', 'Latin America and the Caribbean', '019', '9', '-80', 'Panamanian Balboa', '4176000', 'Arabic,Creole English,Cuna,Embera,Guaym√≠,Spanish', '75000', '745', '.pa');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Papua New Guinea', 'PG', 'PNG', '598', '675', 'PGK', 'Port Moresby', 'Oceania', 'Melanesia', '009', '-6', '147', 'Papua New Guinea Kina', '8606000', 'Malenasian Languages,Papuan Languages', '462000', '-', '.pg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Paraguay', 'PY', 'PRY', '600', '595', 'PYG', 'Asunci', 'Americas', 'Latin America and the Caribbean', '019', '-23', '-58', 'Paraguay Guarani', '6956000', 'German,Guaran√≠,Portuguese,Spanish', '406000', '784', '.py');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Peru', 'PE', 'PER', '604', '51', 'PEN', 'Lima', 'Americas', 'Latin America and the Caribbean', '019', '-10', '-76', 'Peruvian Nuevo Sol', '31900000', 'Aimar√°,Ket¬öua,Spanish', '1285000', '775', '.pe');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Philippines', 'PH', 'PHL', '608', '63', 'PHP', 'Manila', 'Asia', 'South-eastern Asia', '142', '13', '122', 'Philippine Peso', '106600000', 'Bicol,Cebuano,Hiligaynon,Ilocano,Maguindanao,Maranao,Pampango,Pangasinan,Pilipino,Waray-waray', '300000', '480', '.ph');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Pitcairn', 'PN', 'PCN', '612', '64', 'NZD', 'Adamstown', 'Oceania', 'Polynesia', '009', ' -24.7', ' -127.4', '0', '0', 'Pitcairnese', '49', '-', '.pn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Poland', 'PL', 'POL', '616', '48', 'PLN', 'Warszawa', 'Europe', 'Eastern Europe', '150', '52', '20', 'Polish Zloty', '37900000', 'Belorussian,German,Polish,Ukrainian', '323000', '590', '.pl');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Portugal', 'PT', 'PRT', '620', '351', 'EUR', 'Lisboa', 'Europe', 'Southern Europe', '150', ' 39.5', '-8', 'Euro', '10200000', 'Portuguese', '91000', '560', '.pt');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Puerto Rico', 'PR', 'PRI', '630', '1939', 'USD', 'San Juan', 'Americas', 'Latin America and the Caribbean', '019', ' 18.25', ' -66.5', 'US Dollar', '3195000', 'English,Spanish', '8875', '-', '.pr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Qatar', 'QA', 'QAT', '634', '974', 'QAR', 'Doha', 'Asia', 'Western Asia', '142', ' 25.5', ' 51.25', 'Qatari Rial', '2781000', 'Arabic,Urdu', '11000', '-', '.qa');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Reunion', 'RE', 'REU', '638', '262', 'EUR', 'Saint-Denis', 'Africa', 'Sub-Saharan Africa', '002', '-', '-', '0', '859000', 'Chinese,Comorian,Creole French,Malagasy,Tamil', '2510', '-', '.re');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Romania', 'RO', 'ROU', '642', '40', 'RON', 'Bucuresti', 'Europe', 'Eastern Europe', '150', '46', '25', 'Romanian New Leu', '19400000', 'German,Hungarian,Romani,Romanian,Serbo-Croatian,Ukrainian', '238000', '594', '.ro');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Russian Federation', 'RU', 'RUS', '643', '7', 'RUB', 'Moscow', 'Europe', 'Eastern Europe', '150', '60', '100', '0', '144400000', 'Avarian,Bashkir,Belorussian,Chechen,Chuvash,Kazakh,Mari,Mordva,Russian,Tatar,Udmur,Ukrainian', '17000000', '-', '.ru');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Rwanda', 'RW', 'RWA', '646', '250', 'RWF', 'Kigali', 'Africa', 'Sub-Saharan Africa', '002', '-2', '30', 'Rwanda Franc', '12300000', 'French,Rwanda', '26000', '-', '.rw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Saint Barthelemy', 'BL', 'BLM', '652', '-', '-', '-', 'Americas', 'Latin America and the Caribbean', '019', '-', '-', '-', '-', '-', '-', '-', '.gp');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Saint Helena', 'SH', 'SHN', '654', '290', 'SHP', 'Jamestown', 'Africa', 'Sub-Saharan Africa', '002', '-', '-', 'St. Helena Pound', '6000', 'English', '314', '-', '.ac');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Saint Kitts and Nevis', 'KN', 'KNA', '659', '1869', 'XCD', 'Basseterre', 'Americas', 'Latin America and the Caribbean', '019', ' 17.3333', ' -62.75', '0', '52000', 'Creole English,English', '261', '-', '.kn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Saint Lucia', 'LC', 'LCA', '662', '1758', 'XCD', 'Castries', 'Americas', 'Latin America and the Caribbean', '019', ' 13.8833', ' -61.1333', 'East Caribbean Dollar', '181000', 'Creole French,English', '622', '-', '.lc');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Saint Martin (French part)', 'MF', 'MAF', '663', '-', '-', '-', 'Americas', 'Latin America and the Caribbean', '019', '-', '-', '-', '-', '-', '-', '-', '-');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Saint Pierre and Miquelon', 'PM', 'SPM', '666', '508', 'EUR', 'Saint-Pierre', 'Americas', 'Northern America', '019', ' 46.8333', ' -56.3333', ' Euro', '5000', 'French', '242', '-', '.pm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Saint Vincent and the Grenadines', 'VC', 'VCT', '670', '1784', 'XCD', 'Kingstown', 'Americas', 'Latin America and the Caribbean', '019', ' 13.25', ' -61.2', 'East Caribbean Dollar', '110000', 'Creole English,English', '388', '-', '.vc');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Samoa', 'WS', 'WSM', '882', '685', 'WST', 'Apia', 'Oceania', 'Polynesia', '009', ' -13.5833', ' -172.3333', 'Samoan Tala', '196000', 'English,Samoan,Samoan-English', '2831', '-', '.ws');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'San Marino', 'SM', 'SMR', '674', '378', 'EUR', 'San Marino', 'Europe', 'Southern Europe', '150', ' 43.7667', ' 12.4167', 'Euro', '33000', 'Italian', '61', '-', '.sm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Sao Tome and Principe', 'ST', 'STP', '678', '239', 'STD', 'S', 'Africa', 'Sub-Saharan Africa', '002', '1', '7', ' Dobra', '211000', 'Crioulo,French', '964', '-', '.st');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Saudi Arabia', 'SA', 'SAU', '682', '966', 'SAR', 'Riyadh', 'Asia', 'Western Asia', '142', '25', '45', 'Saudi Riyal', '33600000', 'Arabic', '2149000', '628', '.sa');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Senegal', 'SN', 'SEN', '686', '221', 'XOF', 'Dakar', 'Africa', 'Sub-Saharan Africa', '002', '14', '-14', 'CFA Franc BCEAO', '15800000', 'Diola,Ful,Malinke,Serer,Soninke,Wolof', '196000', '604', '.sn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Serbia', 'RS', 'SRB', '688', '381', 'RSD', 'Belgrade', 'Europe', 'Southern Europe', '150', '44', '21', 'Serbian dinar', '6963000', 'Serbian,Hungarian,Slovak,Romanian,Croatian,Rusyn, Albanian,Bulgarian, English', '88000', '860', '.rs');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Seychelles', 'SC', 'SYC', '690', '248', 'SCR', 'Victoria', 'Africa', 'Sub-Saharan Africa', '002', ' -4.5833', ' 55.6667', 'Seychelles Rupee', '96000', 'English,French,Seselwa', '455', '-', '.sc');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Sierra Leone', 'SL', 'SLE', '694', '232', 'SLL', 'Freetown', 'Africa', 'Sub-Saharan Africa', '002', ' 8.5', ' -11.5', 'Sierra Leone Leone', '7650000', 'Bullom-sherbro,Ful,Kono-vai,Kuranko,Limba,Mende,Temne,Yalunka', '71000', '-', '.sl');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Singapore', 'SG', 'SGP', '702', '65', 'SGD', 'Singapore', 'Asia', 'South-eastern Asia', '142', ' 1.3667', ' 103.8', 'Singapore Dollar', '5638000', 'Chinese,Malay,Tamil', '618', '888', '.sg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Sint Maarten (Dutch part)', 'SX', 'SXM', '534', '-', '-', '-', 'Americas', 'Latin America and the Caribbean', '019', '-', '-', '-', '-', '-', '-', '-', '.sx');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Slovakia', 'SK', 'SVK', '703', '421', 'EUR', 'Bratislava', 'Europe', 'Eastern Europe', '150', ' 48.6667', ' 19.5', 'Euro', '5446000', 'Czech and Moravian,Hungarian,Romani,Slovak,Ukrainian and Russian', '49000', '858', '.sk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Slovenia', 'SI', 'SVN', '705', '386', 'EUR', 'Ljubljana', 'Europe', 'Southern Europe', '150', '46', '15', 'Euro', '2073000', 'Hungarian,Serbo-Croatian,Slovene', '20000', '383', '.si');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Solomon Islands', 'SB', 'SLB', '090', '677', 'SBD', 'Honiara', 'Oceania', 'Melanesia', '009', '-8', '159', 'Solomon Islands Dollar', '652000', 'Malenasian Languages,Papuan Languages,Polynesian Languages', '28000', '-', '.sb');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Somalia', 'SO', 'SOM', '706', '252', 'SOS', 'Mogadishu', 'Africa', 'Sub-Saharan Africa', '002', '10', '49', 'Somali Shilling', '15000000', 'Arabic,Somali', '637000', '-', '.so');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'South Africa', 'ZA', 'ZAF', '710', '27', 'ZAR', 'Pretoria', 'Africa', 'Sub-Saharan Africa', '002', '-29', '24', 'South African Rand', '57700000', 'Afrikaans,English,Ndebele,Northsotho,Southsotho,Swazi,Tsonga,Tswana,Venda,Xhosa,Zulu', '1221000', '600 – 601', '.za');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Antarctica', '', 'South Georgia and the South Sandwich Islands', 'GS', 'SGS', '239', '500', 'GBP', '0', 'Americas', 'Latin America and the Caribbean', '019', ' -54.5', '-37', 'Pound Sterling', '0', '-', '3903', '-', '.gs');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'South Sudan', 'SS', 'SSD', '728', '211', 'SSP', 'Juba', 'Africa', 'Sub-Saharan Africa', '002', '8', '30', 'South Sudan Pound', '10900000', '-', '619000', '-', '.ss');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Spain', 'ES', 'ESP', '724', '34', 'EUR', 'Madrid', 'Europe', 'Southern Europe', '150', '40', '-4', 'Euro', '46700000', 'Basque,Catalan,Galecian,Spanish', '505000', '-', '.es');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Sri Lanka', 'LK', 'LKA', '144', '0', 'LKR', '0', 'Asia', 'Southern Asia', '142', '7', '81', '-', '21600000', 'Mixed Languages,Singali,Tamil', '65000', '-', '.lk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Sudan', 'SD', 'SDN', '729', '249', 'SDG', 'Khartum', 'Africa', 'Northern Africa', '002', '15', '30', 'Sudanese Pound', '41800000', 'Arabic,Bari,Beja,Chilluk,Dinka,Fur,Lotuko,Nubian Languages,Nuer,Zande', '1886000', '-', '.sd');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Suriname', 'SR', 'SUR', '740', '597', 'SRD', 'Paramaribo', 'Americas', 'Latin America and the Caribbean', '019', '4', '-56', 'Surinam Dollar', '575000', 'Hindi,Sranantonga', '163000', '-', '.sr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Svalbard and Jan Mayen', 'SJ', 'SJM', '744', '47', 'NOK', 'Longyearbyen', 'Europe', 'Northern Europe', '150', '78', '20', '0', '2000', 'Norwegian,Russian', '62000', '-', '.no');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Sweden', 'SE', 'SWE', '752', '46', 'SEK', 'Stockholm', 'Europe', 'Northern Europe', '150', '62', '15', 'Swedish Krona', '10100000', 'Arabic,Finnish,Norwegian,Southern Slavic Languages,Spanish,Swedish', '449000', '-', '.se');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Switzerland', 'CH', 'CHE', '756', '41', 'CHF', 'Bern', 'Europe', 'Western Europe', '150', '47', '8', 'Swiss Franc', '8513000', 'French,German,Italian,Romansh', '41000', '-', '.ch');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Syria', 'SY', 'SYR', '760', '963', 'SYP', 'Damascus', 'Asia', 'Western Asia', '142', '-', '-', 'Syrian Pound', '16900000', 'Arabic,Kurdish', '185000', '621', '.sy');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Taiwan, Province of China', 'TW', 'TWN', '158', '-', '-', '-', 'Asia', 'Eastern Asia', '142', ' 23.5', '121', '-', '-', '-', '-', '-', '.tw');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Tajikistan', 'TJ', 'TJK', '762', '992', 'TJS', 'Dushanbe', 'Asia', 'Central Asia', '142', '39', '71', 'Tajik Somoni', '9100000', 'Russian,Tadzhik,Uzbek', '143000', '488', '.tj');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Tanzania', 'TZ', 'TZA', '834', '255', 'TZS', 'Dodoma', 'Africa', 'Sub-Saharan Africa', '002', '-', '-', 'Tanzanian Shilling', '56300000', 'Chaga and Pare,Gogo,Ha,Haya,Hehet,Luguru,Makonde,Nyakusa,Nyamwesi,Shambala,Swahili', '883000', '620', '.tz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Thailand', 'TH', 'THA', '764', '66', 'THB', 'Bangkok', 'Asia', 'South-eastern Asia', '142', '15', '100', 'Thai Baht', '69400000', 'Chinese,Khmer,Kuy,Lao,Malay,Thai', '513000', '885', '.th');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Timor-Leste', 'TL', 'TLS', '626', '-', '-', '-', 'Asia', 'South-eastern Asia', '142', ' -8.55', ' 125.5167', '-', '-', '-', '-', '-', '.tl');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Togo', 'TG', 'TGO', '768', '228', 'XOF', 'Lomé', 'Africa', 'Sub-Saharan Africa', '002', '8', ' 1.1667', 'CFA Franc BCEAO', '7889000', 'Ane,Ewe,Gurma,Kaby√©,Kotokoli,Moba,Naudemba,Watyi', '56000', '-', '.tg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Tokelau', 'TK', 'TKL', '772', '690', 'NZD', 'Fakaofo', 'Oceania', 'Polynesia', '009', '-9', '-172', 'New Zealand Dollar', '1000', 'English,Tokelau', '12', '-', '.tk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Tonga', 'TO', 'TON', '776', '676', 'TOP', 'Nukualofa', 'Oceania', 'Polynesia', '009', '-20', '-175', 'Tongan Paanga', '103000', 'English,Tongan', '650', '-', '.to');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Trinidad and Tobago', 'TT', 'TTO', '780', '1868', 'TTD', 'Port-of-Spain', 'Americas', 'Latin America and the Caribbean', '019', '11', '-61', 'Trinidad and Tobago Dollar', '1389000', 'Creole English,English,Hindi', '5130', '-', '.tt');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Tunisia', 'TN', 'TUN', '788', '216', 'TND', 'Tunis', 'Africa', 'Northern Africa', '002', '34', '9', 'Tunisian Dollar', '11500000', 'Arabic,Arabic-French,Arabic-French-English', '163000', '619', '.tn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Turkey', 'TR', 'TUR', '792', '90', 'TRY', 'Ankara', 'Asia', 'Western Asia', '142', '39', '35', 'Turkish Lira', '82300000', 'Arabic,Kurdish,Turkish', '774000', '868 – 869', '.tr');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Turkmenistan', 'TM', 'TKM', '795', '993', 'TMT', 'Ashgabat', 'Asia', 'Central Asia', '142', '40', '60', 'Manat', '5850000', 'Kazakh,Russian,Turkmenian,Uzbek', '488000', '483', '.tm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'Turks and Caicos Islands', 'TC', 'TCA', '796', '1649', 'USD', 'Cockburn Town', 'Americas', 'Latin America and the Caribbean', '019', ' 21.75', ' -71.5833', '0', '37000', 'English', '430', '-', '.tc');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Tuvalu', 'TV', 'TUV', '798', '688', 'AUD', 'Funafuti', 'Oceania', 'Polynesia', '009', '-8', '178', 'Australian Dollar', '11000', 'English,Kiribati,Tuvalu', '26', '-', '.tv');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Uganda', 'UG', 'UGA', '800', '256', 'UGX', 'Kampala', 'Africa', 'Sub-Saharan Africa', '002', '1', '32', 'Uganda Shilling', '42700000', 'Acholi,Ganda,Gisu,Kiga,Lango,Lugbara,Nkole,Rwanda,Soga,Teso', '241000', '-', '.ug');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'Ukraine', 'UA', 'UKR', '804', '380', 'UAH', 'Kyiv', 'Europe', 'Eastern Europe', '150', '49', '32', 'Ukraine Hryvnia', '44600000', 'Belorussian,Bulgariana,Hungarian,Polish,Romanian,Russian,Ukrainian', '603000', '482', '.ua');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'United Arab Emirates', 'AE', 'ARE', '784', '971', 'AED', 'Abu Dhabi', 'Asia', 'Western Asia', '142', '24', '54', 'Arab Emirates Dirham', '9630000', 'Arabic,Hindi', '83000', '629', '.ae');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Europe', '', 'United Kingdom', 'GB', 'GBR', '826', '44', 'GBP', 'London', 'Europe', 'Northern Europe', '150', '54', '-2', '0', '66400000', 'English,Gaeli,Kymri', '242000', '500 – 509', '.uk');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('North America', '', 'United States of America', 'US', 'USA', '840', '1', 'USD', 'Washington', 'Americas', 'Northern America', '019', '38', '-97', 'US Dollar', '326600000', 'Chinese,English,French,German,Italian,Japanese,Korean,Polish,Portuguese,Spanish,Tagalog,Vietnamese', '9363000', '000 – 019', '.us');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'United States Minor Outlying Islands', 'UM', 'UMI', '581', '1', 'USD', 'null ', 'Oceania', 'Micronesia', '009', ' 19.2833', ' 166.6', '0', '0', 'English', '16', '-', '.um');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Uruguay', 'UY', 'URY', '858', '598', 'UYU', 'Montevideo', 'Americas', 'Latin America and the Caribbean', '019', '-33', '-56', 'Uruguayan Peso', '3449000', 'Spanish', '175000', '773', '.uy');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Uzbekistan', 'UZ', 'UZB', '860', '998', 'UZS', 'Toskent', 'Asia', 'Central Asia', '142', '41', '64', 'Uzbekistan Sum', '32900000', 'Karakalpak,Kazakh,Russian,Tadzhik,Tatar,Uzbek', '447000', '478', '.uz');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Vanuatu', 'VU', 'VUT', '548', '678', 'VUV', 'Port-Vila', 'Oceania', 'Melanesia', '009', '-16', '167', 'Vanuatu Vatu', '292000', 'Bislama,English,French', '12000', '-', '.vu');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('South America', '', 'Venezuela', 'VE', 'VEN', '862', '58', 'VEF', 'Caracas', 'Americas', 'Latin America and the Caribbean', '019', '8', '-66', 'Venezuelan Bolivar', '28800000', 'Goajiro,Spanish,Warrau', '912000', '759', '.ve');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Vietnam', 'VN', 'VNM', '704', '84', 'VND', 'Hanoi', 'Asia', 'South-eastern Asia', '142', '16', '106', 'Vietnamese Dong', '95500000', 'Chinese,Khmer,Man,Miao,Muong,Nung,Thai,Tho,Vietnamese', '331000', '893', '.vn');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Virgin Islands (British)', 'VG', 'VGB', '092', '-', '-', '-', 'Americas', 'Latin America and the Caribbean', '019', '-', '-', '-', '-', '-', '-', '-', '.vg');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('-', '', 'Virgin Islands (U.S.)', 'VI', 'VIR', '850', '-', '-', '-', 'Americas', 'Latin America and the Caribbean', '019', '-', '-', '-', '-', '-', '-', '-', '.vi');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Oceania', '', 'Wallis and Futuna', 'WF', 'WLF', '876', '681', 'XPF', 'Mata-Utu', 'Oceania', 'Polynesia', '009', ' -13.3', ' -176.2', '0', '15000', 'Futuna,Wallis', '200', '-', '.wf');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Western Sahara', 'EH', 'ESH', '732', '212', 'MAD', 'El-Aai', 'Africa', 'Northern Africa', '002', ' 24.5', '-13', 'Moroccan Dirham', '652000', 'Arabic', '266000', '-', '.eh');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Asia', '', 'Yemen', 'YE', 'YEM', '887', '967', 'YER', 'Sanaa', 'Asia', 'Western Asia', '142', '15', '48', 'Yemeni Rial', '28400000', 'Arabic,Soqutri', '527000', '-', '.ye');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Zambia', 'ZM', 'ZMB', '894', '260', 'ZMW', 'Lusaka', 'Africa', 'Sub-Saharan Africa', '002', '-15', '30', 'Zambian Kwacha', '17300000', 'Bemba,Chewa,Lozi,Nsenga,Nyanja,Tongan', '752000', '-', '.zm');
            insert into country(continent_name, continent_code, country_name, country_uid, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain) values ('Africa', '', 'Zimbabwe', 'ZW', 'ZWE', '716', '263', 'ZWD', 'Harare', 'Africa', 'Sub-Saharan Africa', '002', '-20', '30', 'Zimbabwe Dollar', '14400000', 'English,Ndebele,Nyanja,Shona', '390000', '-', '.zw');


            insert into client_instance(client_instance_uid, country_uid, client_name, client_code, client_description, start_date, is_internal, is_system, is_test)
            values ('system', 'XX', 'system', 'system', 'System client - default one', now(), 1, 1, 0);
            insert into client_instance(client_instance_uid, country_uid, client_name, client_code, client_description, start_date, is_internal, is_system, is_test)
            values ('test', 'XX', 'test', 'test', 'Test client - just for testing purpose', now(), 1, 1, 1);


            insert into account_title(account_title_uid, title_name, title_description) values ('CEO', 'Chief Execution Officer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('CFO', 'Chief Financial Officer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('CIO', 'Chief Information Officer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('CSO', 'Chief Security Officer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('CMO', 'Chief Marketing Officer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('COO', 'Chief Operating Officer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('CTO', 'Chief Technology Officer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('CCO', 'Chief Communications Officer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('HoE', 'Head of Engineering', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('HoA', 'Head of Analysis', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('HoC', 'Head of Cloud', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('DMgr', 'Delivery Manager', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('DE', 'Data Engineer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('LDE', 'Lead Data Engineer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('CE', 'Cloud Engineer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('LCE', 'Lead Cloud Engineer', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('DA', 'Data Analyst', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('LDA', 'Lead Data Analyst', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('ADM', 'Administrator', '');
            insert into account_title(account_title_uid, title_name, title_description) values ('DEF', 'Default', '');

            insert into account_group(account_group_uid, account_group_name, account_group_description) values ('Default', 'Default', '');



            insert into account_division(account_division_uid, division_name, division_description) values ('Default', 'Default', '');


            insert into account_instance(account_instance_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system)
            values ('system', 'DEF', 'Default', 'Default', 'Internal', '{system_email}', 'system', 'System', 1);
            insert into account_instance(account_instance_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system)
            values ('test', 'DEF', 'Test', 'Test', 'Internal', '{test_email}', 'test', 'Test', 1);
            insert into account_instance(account_instance_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system)
            values ('administrator', 'ADM', 'Default', 'Default', 'Internal', '{administrator_email}', 'Administrator', 'Administrator', 1);

                       insert into auth_role(auth_role_uid, role_name, role_description, parent_auth_role_uid, access_uris, is_project, is_client, is_custom) values ('SystemAdministrator', 'SystemAdministrator', '', 'SystemAdministrator', '', 0, 0, 0);
            insert into auth_role(auth_role_uid, role_name, role_description, parent_auth_role_uid, access_uris, is_project, is_client, is_custom) values ('ReportManager', 'ReportManager', '', 'SystemAdministrator', '', 0, 0, 0);
            insert into auth_role(auth_role_uid, role_name, role_description, parent_auth_role_uid, access_uris, is_project, is_client, is_custom) values ('ClientAdministrator', 'ClientAdministrator', '', 'SystemAdministrator', '', 0, 0, 0);
            insert into auth_role(auth_role_uid, role_name, role_description, parent_auth_role_uid, access_uris, is_project, is_client, is_custom) values ('Supervisor', 'Supervisor', '', 'ClientAdministrator', '', 0, 0, 0);
            insert into auth_role(auth_role_uid, role_name, role_description, parent_auth_role_uid, access_uris, is_project, is_client, is_custom) values ('DeliveryManager', 'DeliveryManager', '', 'ClientAdministrator', '', 0, 0, 0);
            insert into auth_role(auth_role_uid, role_name, role_description, parent_auth_role_uid, access_uris, is_project, is_client, is_custom) values ('Employee', 'Employee', '', 'ClientAdministrator', '', 0, 0, 0);
            insert into auth_role(auth_role_uid, role_name, role_description, parent_auth_role_uid, access_uris, is_project, is_client, is_custom) values ('StandardUser', 'StandardUser', '', '', '', 0, 0, 0);
            insert into auth_role(auth_role_uid, role_name, role_description, parent_auth_role_uid, access_uris, is_project, is_client, is_custom) values ('Everyone', 'Everyone', 'dummy role for everyone', 'StandardUser', '', 0, 0, 0);

            insert into auth_identity(auth_identity_uid, identity_name, identity_type) values ('Internal', 'Internal', 'INTERNAL');
