
  <include file="./changelog0001_common.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0002_system.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0003_dictionary.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0004_location.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0005_connection.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0006_audit.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0007_storage.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0008_synchronization.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0009_monitor.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0010_event.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0011_process.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0012_report.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0020_tenant.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0021_client.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0022_account.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0023_auth.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0024_invoice.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0025_project.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0026_time.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0027_calendar.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0031_rich_views.xml" relativeToChangelogFile="true"/>
  <include file="./changelog0035_data.xml" relativeToChangelogFile="true"/>





drop view xxx;
drop view v_definition_dao_base;
drop view v_definition_read_dto;
drop view v_definition_read_dtos;
drop view v_definition_write_dtos;
drop view v_definition_thin_dto;
drop view v_definition_write_dto;
drop view v_models_register;


drop view v_models;
drop view v_foreign_key_existing;
drop view v_foreign_key;
drop view v_table_column;
drop view v_column_list;

drop view v_table_rich_list;
drop view v_definition_table_base_list;
drop table v_definition_table_all_list;

drop view v_table_base_list;
drop view v_table_list;
drop view v_table_column;
drop view v_models;
drop view v_column_base_list;
drop view v_column_list;
drop view v_column_rich_list;
v_table_column_base;




drop view ;
drop view ;
drop view ;
drop view ;
drop view ;
drop view ;
drop view ;
drop view ;
drop view v_definition_table_column_all;
drop view v_definition_column_all_list;
drop view v_definition_system_table_generation_list;
drop view v_definition_table_custom_list;
drop view v_definition_table_rich_list;
drop view v_definition_table_base_list;
drop view v_definition_table_all_list;




create or replace view v_definition_table_all_list as
	select t.table_name
	, t.table_full_name
	, replace(t.table_name, 'v_rich_', '') as full_name
	, concat('class ', t.table_name, '_dtos(base_dto):') as dtos_class
	, concat('', t.table_name, '_dtos') as dtos_class_name
	, concat('class ', t.table_name, '_write_dto(base_write_dto):') as dto_write_class
	, concat('', t.table_name, '_write_dto') as dto_write_class_name
	, concat('list[', t.table_name, '_write_dto]') as dto_write_class_name_list
	, concat('class ', t.table_name, '_read_dto(base_read_dto, ', t.table_name, '_write_dto):') as dto_read_class_definition
	, concat('', t.table_name, '_read_dto') as dto_read_class_name
	, concat('list[', t.table_name, '_read_dto]') as dto_read_class_name_list
	, concat('', t.table_name, '_thin_dto') as dto_thin_class_name
	, concat('class ', t.table_name, '_dao(base_dao):') as dao_class_definition
	, concat('', t.table_name, '_dao') as dao_class_name
	, concat('class ', t.table_name, '_service(base_service):') as service_class_definition
	, concat('', t.table_name, '_service') as service_class_name
	, concat('class ', t.table_name, '_controller(base_controller):') as controller_class_definition
	, concat('', t.table_name, '_controller') as controller_class_name
	, concat(t.table_name, '_model') as get_model_object_definition
	, '' as empty_line_definition
	, coalesce(tc.table_comment, '') as table_comment
	, case when t.table_full_name not like 'v_%' and t.table_type='BASE TABLE' then 1 else 0 end as is_base
	, case when t.table_full_name like 'v_rich_%' then 1 else 0 end as is_rich
	, case when t.table_full_name like 'v_custom_%' then 1 else 0 end as is_custom
	, case when t.table_full_name like 'v_definition_%' then 1 else 0 end as is_definition
	from
	 (select table_name as table_full_name, replace(table_name, 'v_rich_', '') as table_name, table_type from information_schema.tables where table_schema='public'  and table_name not in ('databasechangeloglock', 'databasechangelog')) t
	 left join (
		 SELECT t.table_name, pg_catalog.obj_description(pgc.oid, 'pg_class') as table_comment
			FROM information_schema.tables t
			INNER JOIN pg_catalog.pg_class pgc ON t.table_name = pgc.relname
			WHERE t.table_type='BASE TABLE'
			AND t.table_schema='public'
	 ) tc on t.table_full_name = tc.table_name
;

create or replace view v_definition_table_base_list as
	select *
	from v_definition_table_all_list
	where is_base=1
;


create or replace view v_definition_table_rich_list as
	select *
	from v_definition_table_all_list
	where is_rich=1
;

create or replace view v_definition_table_custom_list as
	select *
	from v_definition_table_all_list
	where is_custom=1
;

create or replace view v_definition_system_table_generation_list as
	select concat('insert into system_table(system_table_uid, system_table_name, key_name, table_code, table_comment)',
	 ' values (''', t.table_name, ''',''', t.table_name, ''',''',concat(t.table_name, '_uid'), ''', '''', ''', tc.table_comment, ''');') as sql_line
	from information_schema.tables t
	            	 left join (
					 SELECT t.table_name, pg_catalog.obj_description(pgc.oid, 'pg_class') as table_comment
						FROM information_schema.tables t
						INNER JOIN pg_catalog.pg_class pgc ON t.table_name = pgc.relname
						WHERE t.table_type='BASE TABLE'
						AND t.table_schema='public'
				 ) tc on t.table_name = tc.table_name
	WHERE t.table_type='BASE TABLE' and t.table_schema='public' and t.table_name not in ('databasechangeloglock', 'databasechangelog')
	order by t.table_name
;


create or replace view v_definition_column_all_list as
	select table_name as table_full_name
	 , replace(replace(table_name, 'v_rich_', ''), 'v_custom', '') as table_name
	 , column_name
	 , case when column_default like '%replace%' then null else replace(replace(column_default, '::text', ''), 'now()', 'datetime.datetime.now()') end as column_default
	 , concat('self.', column_name) as self_column_name
	 , data_type
	 , is_nullable
	 , ordinal_position
	 , cast(concat(case data_type when 'bigint' then 'int' when 'text' then 'str' when 'timestamp without time zone' then 'datetime.datetime' else 'str' end, '', case when is_nullable='YES' then '| None' else '' end) as text) as python_type
	 , cast(concat( column_name, ': ', case data_type when 'bigint' then 'int' when 'text' then 'str' when 'timestamp without time zone' then 'datetime.datetime' else 'str' end, '', case when is_nullable='YES' then ' | None' else '' end) as text) as python_definition
	 , cast(concat( column_name, ': ', case data_type when 'bigint' then 'int' when 'text' then 'str' when 'timestamp without time zone' then 'datetime.datetime' else 'str' end, '', case when is_nullable='YES' then ' | None' else '' end, ' = ',
	    case when column_name='is_active' then '1' when column_name='custom_attributes' then '"{}"' when column_name='system_version_uid' then 'objects.system_version_uid' when column_name='system_instance_uid' then 'objects.system_instance_uid' when column_name='' then ''  when column_name='' then '' when data_type='bigint' then '0' when data_type='text' then '""' when data_type='timestamp without time zone' then 'datetime.datetime.now()' else '""' end) as text) as python_definition_default
	 --, cast(concat('    ', column_name, ': ', case data_type when 'bigint' then 'int' when 'text' then 'str' when 'timestamp without time zone' then 'datetime.datetime' else 'str' end, '', case when is_nullable='YES' then ' | None' else '' end) as text) as python_definition_class
	 , cast(concat('"', column_name, '": "', case data_type when 'bigint' then 'int' when 'text' then 'str' when 'timestamp without time zone' then 'datetime.datetime' else 'str' end, '', case when is_nullable='YES' then ' | None' else '' end, '"') as text) as python_map_definition
	 , cast(concat(case when column_name='is_active' then '1' when column_name='custom_attributes' then '"{}"' when column_name='' then ''  when column_name='' then '' when data_type='bigint' then '0' when data_type='text' then '""' when data_type='timestamp without time zone' then 'datetime.datetime.now()' else '""' end) as text) as python_empty_value
	 , cast(concat(case when column_name='is_active' then '1' when column_name='created_by' then '"system"' when column_name='custom_attributes' then '"{}"' when column_name='' then '' when column_name=concat(table_name, '_uid') then 'base_dto.get_random_uid()' when data_type='bigint' then '0' when data_type='text' then '""' when data_type='timestamp without time zone' then 'datetime.datetime.now()' else '""' end) as text) as python_default_value
	 , cast(concat(case when column_name='is_active' then '1' when column_name='created_by' then '"system"' when column_name='custom_attributes' then '"{}"' when column_name='' then '' when column_name=concat(table_name, '_uid') then 'base_dto.get_random_uid()' when data_type='bigint' then '0' when data_type='text' then 'base_dto.get_random_uid()' when data_type='timestamp without time zone' then 'datetime.datetime.now()' else '""' end) as text) as python_random_value
	 , cast(concat('        self.', column_name, ' = ', column_name) as text) as self_set
	 , case when column_name  in ('row_instance', 'row_lock', 'row_owner', 'row_seq', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes') then 1 else 0 end as is_metadata
	 , case when column_name  in ('row_instance', 'row_lock', 'row_owner', 'row_seq', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes') then 1 else 0 end as is_value
	 , case when column_name like '%_uid' and column_name<> concat(table_name, '_uid') then 1 else 0 end as is_fk
	 , case when column_name = concat(table_name, '_name') and column_name<> concat(table_name, '_uid') then 1 else 0 end as is_name
	 , case when column_name not in (concat(table_name, '_uid'), 'row_instance', 'row_lock', 'row_owner', 'row_seq', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes') then 1 else 0 end as is_non_key_attribute
	 , case when column_name not in ('row_instance', 'row_lock', 'row_owner', 'row_seq', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes') then 1 else 0 end as is_attribute
	 , case when column_name not in ('row_instance', 'row_lock', 'row_owner', 'row_seq', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by') then 1 else 0 end as is_write
	 , case when table_name not like 'v_%' then 1 else 0 end as is_base
	 , case when table_name like 'v_rich_%' then 1 else 0 end as is_rich
	 , case when table_name like 'v_custom_%' then 1 else 0 end as is_custom
	 , case when table_name like 'v_definition_%' then 1 else 0 end as is_definition
	from information_schema.columns
	where table_schema='public' and table_name not in ('databasechangeloglock', 'databasechangelog')
	order by ordinal_position
;


create or replace view v_definition_column_base_list as
	select *
	from v_definition_column_all_list
	where is_base=1
;

create or replace view v_definition_column_rich_list as
	select *
	from v_definition_column_all_list
	where is_rich=1
;

create or replace view v_definition_column_custom_list as
	select *
	from v_definition_column_all_list
	where is_rich=1
;

create or replace view v_definition_table_column_all as
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
        , allcolls.python_definition_defaults as all_python_definition_defaults
        , allcolls.python_map_definitions as all_python_map_definitions
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
        , attrcols.python_empty_values as attr_python_empty_values
        , attrcols.python_default_values as attr_python_default_values
        , attrcols.python_random_values as attr_python_random_values
        , attrcols.python_definition_defaults as attr_python_definition_defaults
        , attrcols.python_map_definitions as attr_python_map_definitions
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
        , attrnonkeycols.python_definition_defaults as attrnonkey_python_definition_defaults
        , attrnonkeycols.python_map_definitions as attrnonkey_python_map_definitions
        , coalesce(fktbl.fk_definitions, '') as fk_columns_definition
	from v_definition_table_all_list t
	 join (
	 	select table_name, table_full_name
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
	 	 , string_agg(python_definition_default, ', ' order by ordinal_position) as python_definition_defaults
	 	 , string_agg(python_map_definition, ', ' order by ordinal_position) as python_map_definitions
		from v_definition_column_all_list
	 	group by table_name, table_full_name
	 ) allcolls on t.table_full_name = allcolls.table_full_name
	 join (
		select table_name, table_full_name
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
	 	 , string_agg(python_definition_default, ', ' order by ordinal_position) as python_definition_defaults
	 	 , string_agg(python_map_definition, ', ' order by ordinal_position) as python_map_definitions
		from v_definition_column_all_list
		where is_attribute=1
		group by table_name, table_full_name
	 ) attrcols on t.table_full_name = attrcols.table_full_name
	 join (
		select table_name, table_full_name
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
	 	 , string_agg(python_definition_default, ', ' order by ordinal_position) as python_definition_defaults
	 	 , string_agg(python_map_definition, ', ' order by ordinal_position) as python_map_definitions
		from v_definition_column_all_list
		where is_non_key_attribute=1
		group by table_name, table_full_name
	 ) attrnonkeycols on t.table_full_name = attrnonkeycols.table_full_name
	 left join (
	 	select c.table_name, string_agg(concat('"', c.column_name, '": "', fkt.table_name, '"') , ', ' order by ordinal_position) as fk_definitions
		 from v_definition_column_all_list c
		 join v_definition_table_base_list fkt on  c.column_name like concat('%', fkt.table_name, '_uid')
		where c.column_name like '%_uid' and c.table_name <> fkt.table_name
		group by c.table_name
	 ) fktbl on fktbl.table_name = t.table_full_name
;

create or replace view v_definition_table_column_base as
	select *
	from v_definition_table_column_all
	where is_base=1
;

create or replace view v_definition_table_column_rich as
	select *
	from v_definition_table_column_all
	where is_rich=1
;

create or replace view v_definition_table_column_custom as
	select *
	from v_definition_table_column_all
	where is_custom=1
;

--  -------------------------------- FK Liquibase definitions
create or replace view v_definition_foreign_key as
	select c.table_name, c.column_name, fkt.table_name as fk_table_name, concat(fkt.table_name, '_uid') as fk_column_uid,
	 concat('<addForeignKeyConstraint baseTableName="', c.table_name, '" baseColumnNames="', c.column_name, '" constraintName="fk_', c.table_name, '_', c.column_name, '" referencedTableName="', fkt.table_name , '" referencedColumnNames="', fkt.table_name , '_uid" />') as liquibase_definition
	 from v_definition_column_all_list c
	 join v_definition_table_base_list fkt on  c.column_name like concat('%', fkt.table_name, '_uid')
	where c.column_name like '%_uid' and c.table_name <> fkt.table_name
	order by c.table_name, c.ordinal_position
;

--  -------------------------------- FKs
create or replace view v_definition_foreign_key_existing as
	select tc.table_schema, tc.constraint_name, tc.table_name, kcu.column_name, ccu.table_schema AS foreign_table_schema, ccu.table_name AS foreign_table_name, ccu.column_name AS foreign_column_name
	FROM information_schema.table_constraints AS tc
	JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name AND tc.table_schema = kcu.table_schema
	JOIN information_schema.constraint_column_usage AS ccu ON ccu.constraint_name = tc.constraint_name
	where tc.table_schema='public' and tc.constraint_name like 'fk_%'
;


--  -------------------------------- models


create or replace view v_definition_models as
	select t.table_name, 1 as ordinal_position,
	 concat('    ', t.table_name, '_model: base_model = base_model(''', t.table_name, ''', [', t.attr_column_names_list, '], [', coalesce(r.attr_column_names_list, ''), '], {', t.attr_python_map_definitions, '}, {', t.fk_columns_definition ,'}, "', t.table_comment, '")') as python
	from v_definition_table_column_base t
	 left join v_definition_table_column_rich r on t.table_name = r.table_name
	order by t.table_name
;

-- -------------------------------- models registers
create or replace view v_models_register as
	select table_name, 1 as ordinal_position,  concat('        self.all_models["', table_name ,'"] = self.', table_name, '_model') as python
	from v_definition_table_column_base
	order by table_name
;


--------------------------------------- DTO SINGLE CLASSES

-- -------------------------------- write_dto classes: T_write_dto
create or replace view v_definition_python_dtos_write as
	select table_name, ordinal_position, python
	from (
	select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_write - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'import datetime'
	union all select '' as table_name, 3 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 4 as ordinal_position, 'from dataclasses import dataclass, asdict'
	union all select '' as table_name, 5 as ordinal_position, 'import json'
	union all select '' as table_name, 6 as ordinal_position, 'from base.base_objects import objects'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_models import *'
	union all select '' as table_name, 9 as ordinal_position, ''
	union all select '' as table_name, 10 as ordinal_position, ''

	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
	union all select table_name, 110 as ordinal_position, concat('class ', table_name, '_write_dto(base_write_dto):')  as python from v_definition_table_base_list
	union all select table_name, 200+ordinal_position , concat('    ', python_definition) from v_definition_column_base_list where is_attribute=1

	union all select table_name, 400 as ordinal_position, concat('    def __init__(self, ',  attr_column_list_with_type , ', custom_attributes: str = "{}"):') from v_definition_table_column_base
	union all select table_name, 500+ordinal_position , self_set from v_definition_column_base_list where is_attribute=1
	union all select table_name, 599 as ordinal_position, concat('        self.custom_attributes = custom_attributes') from v_definition_table_column_base
	union all select table_name, 1110 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1120 as ordinal_position, '    def empty_write(cls):' as python from v_definition_table_base_list
	union all select table_name, 1130 as ordinal_position, concat('        return cls(', attr_python_empty_values, ')') as python from v_definition_table_column_base
	union all select table_name, 1210 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1220 as ordinal_position, '    def default_write(cls):' as python from v_definition_table_base_list
	union all select table_name, 1230 as ordinal_position, concat('        return cls(', attr_python_default_values, ')') as python from v_definition_table_column_base
	union all select table_name, 1310 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1320 as ordinal_position, '    def random_write(cls):' as python from v_definition_table_base_list
	union all select table_name, 1330 as ordinal_position, concat('        return cls(', attr_python_random_values, ')') as python from v_definition_table_column_base

	union all select table_name, 1410 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1420 as ordinal_position, concat('    def new_write(cls, ', attr_column_list_with_type , '):') as python from v_definition_table_column_base
	union all select table_name, 1430 as ordinal_position, concat('        return cls(', attr_column_list, ')') as python from v_definition_table_column_base

	union all select table_name, 1441 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1442 as ordinal_position, concat('    def new_write_with_defaults(cls, ', attr_python_definition_defaults , '):') as python from v_definition_table_column_base
	union all select table_name, 1443 as ordinal_position, concat('        return cls(', attr_column_list, ')') as python from v_definition_table_column_base

	union all select table_name, 1510 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1520 as ordinal_position, concat('    def new_write_random_uid(cls, ', attrnonkey_column_list_with_type , '):') as python from v_definition_table_column_base
	union all select table_name, 1530 as ordinal_position, concat('        return cls(base_dto.get_random_uid(), ', attrnonkey_column_list, ')') as python from v_definition_table_column_base

	union all select table_name, 1810 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1811 as ordinal_position, '    def get_class_model(cls) -> base_model:' as python from v_definition_table_base_list
	union all select table_name, 1812 as ordinal_position, concat('        return db_models.', table_name, '_model') as python from v_definition_table_base_list

	union all select table_name, 1821 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1822 as ordinal_position, '    def from_dictionary(cls, d: dict[str, any]):' as python from v_definition_table_base_list
	union all select table_name, 1823 as ordinal_position, concat('        return cls(', attr_column_dict_list, ')') as python from v_definition_table_column_base

	union all select table_name, 1900 , concat('    def to_write_dict(self) -> dict:') from v_definition_table_base_list
	union all select table_name, 1901 , concat('        return asdict(self)') from v_definition_table_base_list

	union all select table_name, 2120 as ordinal_position, '    def clone_write(self):' as python from v_definition_table_base_list
	union all select table_name, 2130 as ordinal_position, concat('        return ', dto_write_class_name , '(', attr_column_self_list, ', self.custom_attributes)') as python from v_definition_table_column_base
	union all select table_name, 2210 as ordinal_position, '    def clone_write_new_uid(self):' as python from v_definition_table_base_list
	union all select table_name, 2220 as ordinal_position, concat('        return ', dto_write_class_name , '(base_dto.get_random_uid(), ', attrnonkey_column_self_list, ', self.custom_attributes)') as python from v_definition_table_column_base
	union all select table_name, 2310 as ordinal_position, '    def clone_with_uid(self, uid: str):' as python from v_definition_table_base_list
	union all select table_name, 2320 as ordinal_position, concat('        return ', dto_write_class_name , '(uid, ', attrnonkey_column_self_list, ', self.custom_attributes)') as python from v_definition_table_column_base

	union all select table_name, 3110 as ordinal_position, '    def get_model(self) -> base_model:' as python from v_definition_table_base_list
	union all select table_name, 3111 as ordinal_position, concat('        return db_models.', table_name, '_model') as python from v_definition_table_base_list

	union all select table_name, 3221 as ordinal_position, '    def get_uid(self) -> str:' as python from v_definition_table_base_list
	union all select table_name, 3222 as ordinal_position, concat('        return self.', table_name, '_uid') as python from v_definition_table_base_list
	union all select table_name, 3223 as ordinal_position, '    def get_name(self) -> str:' as python from v_definition_table_base_list
	union all select table_name, 3224 as ordinal_position, concat('        return self.', table_name, '_name') as python from v_definition_table_base_list

	union all select table_name, 3310 as ordinal_position, '    def get_list_values(self) -> list[any]:' as python from v_definition_table_base_list
	union all select table_name, 3311 as ordinal_position, concat('        return [', attr_column_self_list, ', self.custom_attributes]') as python from v_definition_table_column_base

	union all select table_name, 3321 as ordinal_position, '    def get_list_values_no_custom(self) -> list[any]:' as python from v_definition_table_base_list
	union all select table_name, 3322 as ordinal_position, concat('        return [', attr_column_self_list, ']') as python from v_definition_table_column_base

	union all select table_name, 3331 as ordinal_position, '    def get_list_write_update(self, updated_by: str) -> list[any]:' as python from v_definition_table_base_list
	union all select table_name, 3332 as ordinal_position, concat('        return [', attrnonkey_column_self_list, ', self.custom_attributes, updated_by, self.', table_name, '_uid]') as python from v_definition_table_column_base

	union all select table_name, 3341 as ordinal_position, '    def get_list_write_insert(self, created_by: str) -> list[any]:' as python from v_definition_table_base_list
	union all select table_name, 3342 as ordinal_position, concat('        return [self.', table_name, '_uid, ', attrnonkey_column_self_list, ', created_by, created_by, self.custom_attributes]') as python from v_definition_table_column_base

	union all select table_name, 3410 as ordinal_position, '    def get_nonkey_values(self) -> list[any]:' as python from v_definition_table_base_list
	union all select table_name, 3411 as ordinal_position, concat('        return [', attrnonkey_column_self_list, ']') as python from v_definition_table_column_base

	union all select table_name, 3420 as ordinal_position, '    def get_nonkey_values_with_custom(self) -> list[any]:' as python from v_definition_table_base_list
	union all select table_name, 3421 as ordinal_position, concat('        return [', attrnonkey_column_self_list, ', self.custom_attributes]') as python from v_definition_table_column_base

	union all select table_name, 3431 as ordinal_position, '    def to_json_write(self) -> str:' as python from v_definition_table_base_list
	union all select table_name, 3432 as ordinal_position, concat('        return json.dumps(self.to_write_dict())') as python from v_definition_table_column_base

	union all select table_name, 3510 as ordinal_position, '    def compare_uid(self, obj: base_write_dto) -> bool:' as python from v_definition_table_base_list
	union all select table_name, 3520 as ordinal_position, concat('        return self.get_uid() == obj.get_uid()') as python from v_definition_table_column_base

	union all select table_name, 4110 as ordinal_position, '    def update_uid(self, uid: str):' as python from v_definition_table_base_list
	union all select table_name, 4111 as ordinal_position, concat('        self.', table_name ,'_uid = uid') as python from v_definition_table_base_list

	union all select table_name, 4202 as ordinal_position, concat('    def update_uid_attributes(self, ', attr_column_list_with_type  , '):') as python from v_definition_table_column_base
	union all select table_name, 4203+ordinal_position as ordinal_position, concat('        self.', column_name, ' = ', column_name , '') as python from v_definition_column_base_list where is_attribute=1

	union all select table_name, 4302 as ordinal_position, concat('    def update_attributes(self, ', attrnonkey_column_list_with_type , '):') as python from v_definition_table_column_base
	union all select table_name, 4303+ordinal_position as ordinal_position, concat('        self.', column_name, ' = ', column_name , '') as python from v_definition_column_base_list where is_non_key_attribute=1

	--union all select table_name, 2700 as ordinal_position, concat('    def to_read(self) -> ', table_name, '_read_dto:') as python from v_definition_table_base_list
	--union all select table_name, 2800 as ordinal_position, concat('        return ', table_name, '_read_dto(0, ', attr_column_self_list, ', "", 0, 1, datetime.now(), "system", datetime.now(), "system", None, None, "{}")') as python from v_definition_table_column_base

	union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
	union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
	union all select 'zzzzzzzzzzzzzzzz' as table_name, 99999 as ordinal_position, ''
	) x order by x.table_name, x.ordinal_position
;


-- -------------------------------- thin_dto classes: T_thin_dto
create or replace view v_definition_python_dtos_thin as
	select x.table_name, x.ordinal_position, x.python
	from (
	select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_thin - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'import datetime'
	union all select '' as table_name, 3 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 4 as ordinal_position, 'from dataclasses import dataclass, asdict'
	union all select '' as table_name, 5 as ordinal_position, 'import json'
	union all select '' as table_name, 6 as ordinal_position, 'from base.base_objects import objects'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_models import *'
	union all select '' as table_name, 9 as ordinal_position, 'from dto.dtos_write import *'
	union all select '' as table_name, 10 as ordinal_position, ''
	union all select '' as table_name, 11 as ordinal_position, ''

	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
	union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_thin_dto(base_dto):') as python from v_definition_table_base_list

	union all select table_name, 201 , concat('    ', table_name , '_uid: str') from v_definition_table_base_list
	union all select table_name, 202 , concat('    ', table_name , '_name: str') from v_definition_table_base_list
	union all select table_name, 203 , concat('    created_date: datetime.datetime') from v_definition_table_base_list
	union all select table_name, 204 , concat('    is_active: int') from v_definition_table_base_list
	union all select table_name, 210 , concat('    def __init__(self, ', table_name , '_uid: str,', table_name , '_name: str, created_date: datetime.datetime, is_active: int):') from v_definition_table_base_list
	union all select table_name, 211 , concat('        self.', table_name , '_uid = ', table_name , '_uid') from v_definition_table_base_list
	union all select table_name, 212 , concat('        self.', table_name , '_name = ', table_name , '_name') from v_definition_table_base_list
	union all select table_name, 213 , concat('        self.created_date = created_date') from v_definition_table_base_list
	union all select table_name, 214 , concat('        self.is_active = is_active') from v_definition_table_base_list

	union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
	union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
	union all select 'zzzzzzzzzzzzzzzz' as table_name, 99999 as ordinal_position, '# auto-generated - v_definition_python_dtos_thin - END'
	) x order by x.table_name, x.ordinal_position
;


-- -------------------------------- read_dto classes: T_read_dto
create or replace view v_definition_python_dtos_read as
	select x.table_name, x.ordinal_position, x.python
	from (
	select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_read - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'import datetime'
	union all select '' as table_name, 3 as ordinal_position, 'from datetime import datetime'
	union all select '' as table_name, 4 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 5 as ordinal_position, 'from dataclasses import dataclass'
	union all select '' as table_name, 6 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos_thin import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_write import *'

	union all select '' as table_name, 10 as ordinal_position, ''
	union all select '' as table_name, 11 as ordinal_position, ''
	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
	union all select table_name, 110 as ordinal_position, dto_read_class_definition as python from v_definition_table_base_list
	union all select table_name, 200+ordinal_position , concat('    ', python_definition) from v_definition_column_base_list
	union all select table_name, 400 as ordinal_position, all_init_definition from v_definition_table_column_base
	union all select table_name, 500+ordinal_position , self_set from v_definition_column_base_list

	union all select table_name, 1110 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1120 as ordinal_position, '    def empty_read(cls):' as python from v_definition_table_base_list
	union all select table_name, 1130 as ordinal_position, concat('        return cls(0, ', attr_python_empty_values, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_definition_table_column_base
	union all select table_name, 1210 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1220 as ordinal_position, '    def default_read(cls):' as python from v_definition_table_base_list
	union all select table_name, 1230 as ordinal_position, concat('        return cls(0, ', attr_python_default_values, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_definition_table_column_base
	union all select table_name, 1310 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1320 as ordinal_position, '    def random_read(cls):' as python from v_definition_table_base_list
	union all select table_name, 1330 as ordinal_position, concat('        return cls(0, ', attr_python_random_values, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_definition_table_column_base

	union all select table_name, 1410 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1420 as ordinal_position, concat('    def new_read_default(cls, ', attr_column_list_with_type , '):') as python from v_definition_table_column_base
	union all select table_name, 1430 as ordinal_position, concat('        return cls(0, ', attr_column_list, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")') as python from v_definition_table_column_base

	union all select table_name, 1510 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1520 as ordinal_position, concat('    def new_read_full(cls, ', all_column_list_with_type , '):') as python from v_definition_table_column_base
	union all select table_name, 1530 as ordinal_position, concat('        return cls(', all_column_list, ')') as python from v_definition_table_column_base

	union all select table_name, 1610 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1620 as ordinal_position, concat('    def from_write(cls, dto: ', dto_write_class_name, '):') as python from v_definition_table_base_list
	union all select table_name, 1630 as ordinal_position, concat('        return cls(0, ', attr_column_dto_list, ', "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)') as python from v_definition_table_column_base

	union all select table_name, 1710 as ordinal_position, '    def clone_read(self):' as python from v_definition_table_base_list
	union all select table_name, 1711 as ordinal_position, concat('        return ', dto_read_class_name , '(', all_column_self_list, ')') as python from v_definition_table_column_base
	--union all select table_name, 1720 as ordinal_position, '    def clone_read_new_uid(self):' as python from v_definition_table_base_list
	--union all select table_name, 1721 as ordinal_position, concat('        return ', dto_read_class_name , '(base_dto.get_random_uid(), ', attrnonkey_column_self_list, ')') as python from v_definition_table_base_list
	--union all select table_name, 1730 as ordinal_position, '    def clone_read_with_uid(self, uid: str):' as python from v_definition_table_base_list
	--union all select table_name, 1731 as ordinal_position, concat('        return ', dto_read_class_name , '(uid, ', attrnonkey_column_self_list, ')') as python from v_definition_table_base_list

	union all select table_name, 1721 as ordinal_position, '    @classmethod' as python from v_definition_table_base_list
	union all select table_name, 1722 as ordinal_position, '    def from_dictionary(cls, d: dict[str, any]):' as python from v_definition_table_base_list
	union all select table_name, 1723 as ordinal_position, concat('        return cls(', all_column_dict_list, ')') as python from v_definition_table_column_base

	union all select table_name, 1731 , concat('    def to_read_dict(self) -> dict:') from v_definition_table_base_list
	union all select table_name, 1732 , concat('        return asdict(self)') from v_definition_table_base_list

	union all select table_name, 1800 as ordinal_position, concat('    def to_write(self) -> ', dto_write_class_name, ':') as python from v_definition_table_base_list
	union all select table_name, 1801 as ordinal_position, concat('        return ', dto_write_class_name, '(', attr_column_self_list, ', self.custom_attributes)') as python from v_definition_table_column_base

	union all select table_name, 1810 as ordinal_position, concat('    def to_thin(self) -> ', table_name, '_thin_dto:') as python from v_definition_table_base_list
	union all select table_name, 1811 as ordinal_position, concat('        return ', table_name, '_thin_dto(self.', table_name, '_uid, self.', table_name, '_name, self.created_date, self.is_active)') as python from v_definition_table_base_list

	union all select table_name, 1910 as ordinal_position, '    def touch(self, updated_by: str = "system"):' as python from v_definition_table_base_list
	union all select table_name, 1911 as ordinal_position, concat('        self.last_updated_date = datetime.datetime.now()') as python from v_definition_table_base_list
	union all select table_name, 1912 as ordinal_position, concat('        self.last_updated_by = updated_by') as python from v_definition_table_base_list
	union all select table_name, 1913 as ordinal_position, concat('        self.row_version = self.row_version+1') as python from v_definition_table_base_list

	union all select table_name, 2300 as ordinal_position, '    def get_list_all_values(self) -> list[any]:' as python from v_definition_table_base_list
	union all select table_name, 2301 as ordinal_position, concat('        return ', all_column_dictionary, '') as python from v_definition_table_column_base

	union all select table_name, 2310 as ordinal_position, '    def get_list_update_values(self, updated_by: str) -> list[any]:' as python from v_definition_table_base_list
	union all select table_name, 2311 as ordinal_position, concat('        return [', attrnonkey_column_self_list, ', self.custom_attributes, updated_by, self.', table_name, '_uid]') as python from v_definition_table_column_base

	union all select table_name, 2400 as ordinal_position, '    def is_older_than(self, dt: datetime.datetime) -> bool:' as python from v_definition_table_base_list
	union all select table_name, 2410 as ordinal_position, concat('        return self.created_date < dt') as python from v_definition_table_base_list
	union all select table_name, 2500 as ordinal_position, '    def is_newer_than(self, dt: datetime.datetime) -> bool:' as python from v_definition_table_base_list
	union all select table_name, 2510 as ordinal_position, concat('        return self.created_date > dt') as python from v_definition_table_base_list

	union all select table_name, 2600 as ordinal_position, '    def to_json_read(self) -> str:' as python from v_definition_table_base_list
	union all select table_name, 2610 as ordinal_position, concat('        return json.dumps(self.to_read_dict())') as python from v_definition_table_base_list

	union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
	union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
	union all select 'zzzzzzzzzzzzzzzz' as table_name, 99999 as ordinal_position, '# auto-generated - v_definition_python_dtos_read - END'
	) x order by x.table_name, x.ordinal_position
;

-- -------------------------------- rich_dto classes: T_rich_dto
create or replace view v_definition_python_dtos_rich as
	select x.table_name, x.ordinal_position, x.python
	from (
	select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_rich - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'import datetime'
	union all select '' as table_name, 3 as ordinal_position, 'from datetime import datetime'
	union all select '' as table_name, 4 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 5 as ordinal_position, 'from dataclasses import dataclass'
	union all select '' as table_name, 6 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos_thin import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_write import *'

	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_rich_list
	union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_rich_dto(', table_name, '_read_dto):') as python from v_definition_table_rich_list
	union all select table_name, 200+ordinal_position , concat('    ', python_definition) from v_definition_column_rich_list
	union all select table_name, 400 as ordinal_position, all_init_definition from v_definition_table_column_rich
	union all select table_name, 1731 , concat('    def to_rich_dict(self) -> dict:') from v_definition_table_rich_list
	union all select table_name, 500+ordinal_position , self_set from v_definition_column_rich_list

	union all select table_name, 1731 , concat('    def to_rich_dict(self) -> dict:') from v_definition_table_rich_list
	union all select table_name, 1732 , concat('        return asdict(self)') from v_definition_table_rich_list

	union all select table_name, 2300 as ordinal_position, '    def get_rich_all_values(self) -> list[any]:' as python from v_definition_table_rich_list
	union all select table_name, 2301 as ordinal_position, concat('        return ', all_column_dictionary, '') as python from v_definition_table_column_rich


	union all select table_name, 99900 , empty_line_definition from v_definition_table_rich_list
	union all select table_name, 99901 , empty_line_definition from v_definition_table_rich_list
	) x order by x.table_name, x.ordinal_position
	;




-- -------------------------------- full_dto classes: T_full_dto
create or replace view v_definition_python_dtos_full as
	select x.table_name, x.ordinal_position, x.python
	from (
	select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_full - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'import datetime'
	union all select '' as table_name, 3 as ordinal_position, 'from datetime import datetime'
	union all select '' as table_name, 4 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 5 as ordinal_position, 'from dataclasses import dataclass'
	union all select '' as table_name, 6 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos_thin import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_write import *'
	union all select '' as table_name, 9 as ordinal_position, 'from dto.dtos_read import *'
	union all select '' as table_name, 10 as ordinal_position, ''
	union all select '' as table_name, 11 as ordinal_position, ''

	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
	union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_full_dto(', table_name, '_read_dto):') as python from v_definition_table_base_list

	union all select table_name, 204 , concat('    is_active: int') from v_definition_table_base_list
	union all select table_name, 210 , concat('    def __init__(self):') from v_definition_table_base_list
	union all select table_name, 214 , concat('        self.is_active = 1') from v_definition_table_base_list

	union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
	union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
	union all select 'zzzzzzzzzzzzzzzz' as table_name, 99999 as ordinal_position, '# auto-generated - v_definition_python_dtos_full - END' as python
	) x order by x.table_name, x.ordinal_position
	;





--------------------------------------- DTOS LIST


-- -------------------------------- read_dtos classes list:  T_read_dtos
create or replace view v_definition_python_dtos_read_list as
	select x.table_name, x.ordinal_position, x.python
	from (
	select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_read_list - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'from __future__ import annotations'
	union all select '' as table_name, 3 as ordinal_position, 'from datetime import datetime'
	union all select '' as table_name, 4 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 5 as ordinal_position, 'from dataclasses import dataclass'
	union all select '' as table_name, 6 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos_thin import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_write import *'
	union all select '' as table_name, 9 as ordinal_position, 'from dto.dtos_read import *'
	union all select '' as table_name, 10 as ordinal_position, 'import datetime'
	union all select '' as table_name, 11 as ordinal_position, 'from typing import Dict, Callable'
	union all select '' as table_name, 10 as ordinal_position, ''
	union all select '' as table_name, 11 as ordinal_position, ''

	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
	union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_read_dtos(base_read_dtos):') as python from v_definition_table_base_list
	union all select table_name, 210 , concat('    dtos: list[', table_name , '_read_dto]') from v_definition_table_base_list
	union all select table_name, 220 , concat('    def __init__(self, dtos: list[', table_name , '_read_dto]):') from v_definition_table_base_list
	union all select table_name, 230 , '        super().__init__(dtos)' from v_definition_table_base_list
	union all select table_name, 231 , '        self.dtos = dtos' from v_definition_table_base_list

	union all select table_name, 300 , '    @classmethod' from v_definition_table_base_list
	union all select table_name, 301 , '    def empty_list(cls):' from v_definition_table_base_list
	union all select table_name, 302 , '        return cls(list())' from v_definition_table_base_list

	union all select table_name, 310 , '    @classmethod' from v_definition_table_base_list
	union all select table_name, 311 , concat('    def from_list(cls, dtos: list[', table_name , '_read_dto]):') from v_definition_table_base_list
	union all select table_name, 312 , '        return cls(dtos)' from v_definition_table_base_list

	union all select table_name, 320 , '    @classmethod' from v_definition_table_base_list
	union all select table_name, 321 , concat('    def from_object(cls, dto: ', table_name , '_read_dto):') from v_definition_table_base_list
	union all select table_name, 322 , '        return cls(list([dto]))' from v_definition_table_base_list

	union all select table_name, 330 , '    @classmethod' from v_definition_table_base_list
	union all select table_name, 331 , concat('    def from_lists(cls, dtos1: list[', table_name , '_read_dto], dtos2: list[', table_name , '_read_dto]):') from v_definition_table_base_list
	union all select table_name, 332 , '        return cls(dtos1 + dtos2)' from v_definition_table_base_list

	union all select table_name, 501 , concat('    def get_active(self):') from v_definition_table_base_list
	union all select table_name, 502 , concat('        return ', table_name, '_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))') from v_definition_table_base_list

	union all select table_name, 511 , concat('    def get_inactive(self):') from v_definition_table_base_list
	union all select table_name, 512 , concat('        return ', table_name, '_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))') from v_definition_table_base_list

	union all select table_name, 521 , concat('    def get_write_dtos(self) -> list[', table_name , '_write_dto]:') from v_definition_table_base_list
	union all select table_name, 522 , concat('        return list(map(lambda x: x.to_write(), self.dtos))') from v_definition_table_base_list

	union all select table_name, 531 , concat('    def get_write_dicts(self) -> list[dict]:') from v_definition_table_base_list
	union all select table_name, 532 , concat('        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))') from v_definition_table_base_list

	union all select table_name, 541 , concat('    def get_read_dicts(self) -> list[dict]:') from v_definition_table_base_list
	union all select table_name, 542 , concat('        return list(map(lambda x: x.to_write_dict(), self.dtos))') from v_definition_table_base_list

	union all select table_name, 551 , concat('    def find_by_uid(self, uid: str) -> ', table_name, '_read_dto | None:') from v_definition_table_base_list
	union all select table_name, 552 , concat('        found_dtos = list(filter(lambda x: x.', table_name, '_uid == uid, self.dtos))') from v_definition_table_base_list
	union all select table_name, 553 , concat('        if (len(found_dtos)>0):') from v_definition_table_base_list
	union all select table_name, 554 , concat('            return found_dtos[0]') from v_definition_table_base_list
	union all select table_name, 555 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 556 , concat('            return None') from v_definition_table_base_list

	union all select table_name, 1001 , concat('    def get_first(self) -> ', table_name, '_read_dto | None:') from v_definition_table_base_list
	union all select table_name, 1002 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
	union all select table_name, 1003 , concat('            return self.dtos[0]') from v_definition_table_base_list
	union all select table_name, 1004 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 1005 , concat('            return None') from v_definition_table_base_list

	union all select table_name, 1011 , concat('    def get_first_n(self, n: int) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
	union all select table_name, 1012 , concat('        if len(self.dtos) > n:') from v_definition_table_base_list
	union all select table_name, 1013 , concat('            return ', table_name, '_read_dtos(self.dtos[:n])') from v_definition_table_base_list
	union all select table_name, 1014 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 1015 , concat('            return ', table_name, '_read_dtos(self.dtos)') from v_definition_table_base_list

	union all select table_name, 1021 , concat('    def get_last(self) -> ', table_name, '_read_dto | None:') from v_definition_table_base_list
	union all select table_name, 1022 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
	union all select table_name, 1023 , concat('            return self.dtos[-1]') from v_definition_table_base_list
	union all select table_name, 1024 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 1025 , concat('            return None') from v_definition_table_base_list

	union all select table_name, 1091 , concat('    def to_dict_by_uid(self) -> dict[str, ', table_name, '_read_dto]:') from v_definition_table_base_list
	union all select table_name, 1092 , concat('        d = {}') from v_definition_table_base_list
	union all select table_name, 1093 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 1094 , concat('            d[dto.get_uid()] = dto') from v_definition_table_base_list
	union all select table_name, 1095 , concat('        return d') from v_definition_table_base_list

	union all select table_name, 1101+ordinal_position*10, concat('    def to_dict_by_', column_name , '(self) -> dict[str, ', table_name, '_read_dto]:') from v_definition_column_base_list where is_attribute = 1
	union all select table_name, 1102+ordinal_position*10, concat('        d = {}') from v_definition_column_base_list where is_attribute = 1
	union all select table_name, 1103+ordinal_position*10, concat('        for dto in self.dtos:') from v_definition_column_base_list where is_attribute = 1
	union all select table_name, 1104+ordinal_position*10, concat('            d[dto.', column_name , '] = dto') from v_definition_column_base_list where is_attribute = 1
	union all select table_name, 1105+ordinal_position*10, concat('        return d') from v_definition_column_base_list where is_attribute = 1

	union all select table_name, 2011 , concat('    def for_each(self, do_method: Callable):') from v_definition_table_base_list
	union all select table_name, 2012 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2013 , concat('            do_method(dto)') from v_definition_table_base_list

	union all select table_name, 2014 , concat('    def for_first(self, do_method: Callable):') from v_definition_table_base_list
	union all select table_name, 2015 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
	union all select table_name, 2016 , concat('            return do_method(self.dtos[0])') from v_definition_table_base_list

	union all select table_name, 2017 , concat('    def for_filter(self, check_method: Callable[[', table_name, '_read_dto], bool], do_method: Callable):') from v_definition_table_base_list
	union all select table_name, 2018 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2019 , concat('            if check_method(dto):') from v_definition_table_base_list
	union all select table_name, 2020 , concat('                do_method(dto)') from v_definition_table_base_list

	union all select table_name, 2021 , concat('    def check_all(self, check_method: Callable[[', table_name, '_read_dto], bool]) -> bool:') from v_definition_table_base_list
	union all select table_name, 2022 , concat('        init = True') from v_definition_table_base_list
	union all select table_name, 2023 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2024 , concat('            init = init and check_method(dto)') from v_definition_table_base_list
	union all select table_name, 2025 , concat('        return False') from v_definition_table_base_list

	union all select table_name, 2031 , concat('    def check_any(self, check_method: Callable[[', table_name, '_read_dto], bool]) -> bool:') from v_definition_table_base_list
	union all select table_name, 2032 , concat('        init = False') from v_definition_table_base_list
	union all select table_name, 2033 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2034 , concat('            init = init or check_method(dto)') from v_definition_table_base_list
	union all select table_name, 2035 , concat('        return False') from v_definition_table_base_list

	union all select table_name, 2041 , concat('    def map_to_string(self, map_method: Callable[[', table_name, '_read_dto], str]) -> list[str]:') from v_definition_table_base_list
	union all select table_name, 2042 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list
	union all select table_name, 2043 , concat('    def map_to_int(self, map_method: Callable[[', table_name, '_read_dto], int]) -> list[int]:') from v_definition_table_base_list
	union all select table_name, 2044 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list
	union all select table_name, 2045 , concat('    def map_to_float(self, map_method: Callable[[', table_name, '_read_dto], float]) -> list[float]:') from v_definition_table_base_list
	union all select table_name, 2046 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list

	union all select table_name, 2051 , concat('    def aggregate_string(self, map_method: Callable[[str, ', table_name, '_read_dto], str], init: str = "") -> str:') from v_definition_table_base_list
	union all select table_name, 2052 , concat('        init_value = init') from v_definition_table_base_list
	union all select table_name, 2053 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2054 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
	union all select table_name, 2055 , concat('        return init_value') from v_definition_table_base_list

	union all select table_name, 2061 , concat('    def aggregate_int(self, map_method: Callable[[int, ', table_name, '_read_dto], int], init: int = 0) -> int:') from v_definition_table_base_list
	union all select table_name, 2062 , concat('        init_value = init') from v_definition_table_base_list
	union all select table_name, 2063 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2064 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
	union all select table_name, 2065 , concat('        return init_value') from v_definition_table_base_list

	union all select table_name, 2071 , concat('    def aggregate_float(self, map_method: Callable[[float, ', table_name, '_read_dto], float], init: float = 0) -> float:') from v_definition_table_base_list
	union all select table_name, 2072 , concat('        init_value = init') from v_definition_table_base_list
	union all select table_name, 2073 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2074 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
	union all select table_name, 2075 , concat('        return init_value') from v_definition_table_base_list

	union all select table_name, 2101 , concat('    def filter(self, filter_method: Callable[[', table_name, '_read_dto], bool]) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
	union all select table_name, 2102 , concat('        return ', table_name, '_read_dtos(list(filter(filter_method, self.dtos)))') from v_definition_table_base_list

	union all select table_name, 2111 , concat('    def group_by(self, group_method: Callable[[', table_name, '_read_dto], str]) -> dict[str, ', table_name, '_read_dtos]:') from v_definition_table_base_list
	union all select table_name, 2112 , concat('        grp_data: dict[str, ', table_name, '_read_dtos] = {}') from v_definition_table_base_list
	union all select table_name, 2113 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2114 , concat('            key = group_method(dto)') from v_definition_table_base_list
	union all select table_name, 2115 , concat('            grp_list = grp_data[key]') from v_definition_table_base_list
	union all select table_name, 2116 , concat('            if grp_list is None:') from v_definition_table_base_list
	union all select table_name, 2117 , concat('                grp_list = ', table_name, '_read_dtos([])') from v_definition_table_base_list
	union all select table_name, 2118 , concat('                grp_data[key] = grp_list') from v_definition_table_base_list
	union all select table_name, 2119 , concat('            grp_list.dtos.append(dto)') from v_definition_table_base_list
	union all select table_name, 2120 , concat('        return grp_data') from v_definition_table_base_list

	union all select table_name, 2131 , concat('    def aggregate_by(self, group_method: Callable[[', table_name, '_read_dto], str], agg_method: Callable[[', table_name, '_read_dtos], any]) -> dict[str, any]:') from v_definition_table_base_list
	union all select table_name, 2132 , concat('        grp_data: dict[str, ', table_name, '_read_dtos] = self.group_by(group_method)') from v_definition_table_base_list
	union all select table_name, 2133 , concat('        res: dict[str, any] = {}') from v_definition_table_base_list
	union all select table_name, 2134 , concat('        for key in grp_data:') from v_definition_table_base_list
	union all select table_name, 2135 , concat('            value = agg_method(grp_data[key])') from v_definition_table_base_list
	union all select table_name, 2136 , concat('            res[key] = value') from v_definition_table_base_list
	union all select table_name, 2137 , concat('        return res') from v_definition_table_base_list

	union all select table_name, 2201 , concat('    def find(self, check_method: Callable[[', table_name, '_read_dto], bool]) -> ', table_name, '_read_dto | None:') from v_definition_table_base_list
	union all select table_name, 2202 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2203 , concat('            if check_method(dto):') from v_definition_table_base_list
	union all select table_name, 2204 , concat('                return dto') from v_definition_table_base_list
	union all select table_name, 2205 , concat('        return None') from v_definition_table_base_list

	union all select table_name, 2301 , concat('    def compare_by(self, value_method: Callable[[', table_name, '_read_dto], any], compare_method: Callable[[any, any], bool]) -> ', table_name, '_read_dto | None:') from v_definition_table_base_list
	union all select table_name, 2302 , concat('        if len(self.dtos) == 0:') from v_definition_table_base_list
	union all select table_name, 2303 , concat('            return None') from v_definition_table_base_list
	union all select table_name, 2304 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 2305 , concat('            max_value = value_method(self.dtos[0])') from v_definition_table_base_list
	union all select table_name, 2306 , concat('            max_elem = self.dtos[0]') from v_definition_table_base_list
	union all select table_name, 2307 , concat('            for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2308 , concat('                next_value = value_method(dto)') from v_definition_table_base_list
	union all select table_name, 2309 , concat('                if compare_method(next_value, max_value):') from v_definition_table_base_list
	union all select table_name, 2310 , concat('                    max_value = next_value') from v_definition_table_base_list
	union all select table_name, 2311 , concat('                    max_elem = dto') from v_definition_table_base_list
	union all select table_name, 2312 , concat('            return max_elem') from v_definition_table_base_list

	union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
	union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
	union all select 'zzzzzzzzzzzzzzzz' as table_name, 99999 as ordinal_position, '# auto-generated - v_definition_python_dtos_full - END' as python
	) x order by x.table_name, x.ordinal_position
	;




-- -------------------------------- write_dtos classes list: T_write_dtos
create or replace view v_definition_python_dtos_write_list as
select x.table_name, x.ordinal_position, x.python
from (
	select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_write_list - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'from __future__ import annotations'
	union all select '' as table_name, 3 as ordinal_position, 'from datetime import datetime'
	union all select '' as table_name, 4 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 5 as ordinal_position, 'from dataclasses import dataclass'
	union all select '' as table_name, 6 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos_thin import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_write import *'
	union all select '' as table_name, 9 as ordinal_position, 'from dto.dtos_read import *'
	union all select '' as table_name, 10 as ordinal_position, 'import datetime'
	union all select '' as table_name, 11 as ordinal_position, 'from typing import Dict, Callable'
	union all select '' as table_name, 10 as ordinal_position, ''
	union all select '' as table_name, 11 as ordinal_position, ''

	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
	union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_write_dtos(base_write_dtos):') as python from v_definition_table_base_list
	union all select table_name, 210 , concat('    dtos: list[', table_name , '_write_dto]') from v_definition_table_base_list
	union all select table_name, 220 , concat('    def __init__(self, dtos: list[', table_name , '_write_dto]):') from v_definition_table_base_list
	union all select table_name, 230 , '        super().__init__(dtos)' from v_definition_table_base_list
	union all select table_name, 231 , '        self.dtos = dtos' from v_definition_table_base_list

	union all select table_name, 300 , '    @classmethod' from v_definition_table_base_list
	union all select table_name, 301 , '    def empty_list(cls):' from v_definition_table_base_list
	union all select table_name, 302 , '        return cls(list())' from v_definition_table_base_list

	union all select table_name, 310 , '    @classmethod' from v_definition_table_base_list
	union all select table_name, 311 , concat('    def from_list(cls, dtos: list[', table_name , '_write_dto]):') from v_definition_table_base_list
	union all select table_name, 312 , '        return cls(dtos)' from v_definition_table_base_list

	union all select table_name, 320 , '    @classmethod' from v_definition_table_base_list
	union all select table_name, 321 , concat('    def from_object(cls, dto: ', table_name , '_write_dto):') from v_definition_table_base_list
	union all select table_name, 322 , '        return cls([dto])' from v_definition_table_base_list

	union all select table_name, 330 , '    @classmethod' from v_definition_table_base_list
	union all select table_name, 331 , concat('    def from_lists(cls, dtos1: list[', table_name , '_write_dto], dtos2: list[', table_name , '_write_dto]):') from v_definition_table_base_list
	union all select table_name, 332 , '        return cls(dtos1 + dtos2)' from v_definition_table_base_list

	union all select table_name, 431 , concat('    def get_write_dicts(self) -> list[dict]:') from v_definition_table_base_list
	union all select table_name, 432 , concat('        return list(map(lambda x: x.to_write_dict(), self.dtos))') from v_definition_table_base_list

	union all select table_name, 451 , concat('    def find_by_uid(self, uid: str) -> ', table_name, '_write_dto | None:') from v_definition_table_base_list
	union all select table_name, 452 , concat('        found_dtos = list(filter(lambda x: x.', table_name, '_uid == uid, self.dtos))') from v_definition_table_base_list
	union all select table_name, 453 , concat('        if (len(found_dtos)>0):') from v_definition_table_base_list
	union all select table_name, 454 , concat('            return found_dtos[0]') from v_definition_table_base_list
	union all select table_name, 455 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 456 , concat('            return None') from v_definition_table_base_list

	union all select table_name, 461 , concat('    def map_by_uid(self) -> dict[str, ', table_name , '_write_dto]:') from v_definition_table_base_list
	union all select table_name, 462 , concat('        res = {}') from v_definition_table_base_list
	union all select table_name, 463 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 464 , concat('            res[dto.', table_name , '_uid] = dto') from v_definition_table_base_list
	union all select table_name, 465 , concat('        return res') from v_definition_table_base_list


	union all select table_name, 501 , concat('    def get_active(self):') from v_definition_table_base_list
	union all select table_name, 502 , concat('        return ', table_name, '_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))') from v_definition_table_base_list

	union all select table_name, 511 , concat('    def get_inactive(self):') from v_definition_table_base_list
	union all select table_name, 512 , concat('        return ', table_name, '_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))') from v_definition_table_base_list

	union all select table_name, 1001 , concat('    def get_first(self) -> ', table_name, '_write_dto | None:') from v_definition_table_base_list
	union all select table_name, 1002 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
	union all select table_name, 1003 , concat('            return self.dtos[0]') from v_definition_table_base_list
	union all select table_name, 1004 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 1005 , concat('            return None') from v_definition_table_base_list

	union all select table_name, 1011 , concat('    def get_first_n(self, n: int) -> ', table_name, '_write_dtos:') from v_definition_table_base_list
	union all select table_name, 1012 , concat('        if len(self.dtos) > n:') from v_definition_table_base_list
	union all select table_name, 1013 , concat('            return ', table_name, '_write_dtos(self.dtos[:n])') from v_definition_table_base_list
	union all select table_name, 1014 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 1015 , concat('            return ', table_name, '_write_dtos(self.dtos)') from v_definition_table_base_list

	union all select table_name, 1021 , concat('    def get_last(self) -> ', table_name, '_write_dto | None:') from v_definition_table_base_list
	union all select table_name, 1022 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
	union all select table_name, 1023 , concat('            return self.dtos[-1]') from v_definition_table_base_list
	union all select table_name, 1024 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 1025 , concat('            return None') from v_definition_table_base_list

	union all select table_name, 1091 , concat('    def to_dict_by_uid(self) -> dict[str, ', table_name, '_write_dto]:') from v_definition_table_base_list
	union all select table_name, 1092 , concat('        d = {}') from v_definition_table_base_list
	union all select table_name, 1093 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 1094 , concat('            d[dto.get_uid()] = dto') from v_definition_table_base_list
	union all select table_name, 1095 , concat('        return d') from v_definition_table_base_list

	union all select table_name, 2011 , concat('    def for_each(self, do_method: Callable):') from v_definition_table_base_list
	union all select table_name, 2012 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2013 , concat('            do_method(dto)') from v_definition_table_base_list

	union all select table_name, 2014 , concat('    def for_first(self, do_method: Callable):') from v_definition_table_base_list
	union all select table_name, 2015 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
	union all select table_name, 2016 , concat('            return do_method(self.dtos[0])') from v_definition_table_base_list

	union all select table_name, 2017 , concat('    def for_filter(self, check_method: Callable[[', table_name, '_write_dto], bool], do_method: Callable):') from v_definition_table_base_list
	union all select table_name, 2018 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2019 , concat('            if check_method(dto):') from v_definition_table_base_list
	union all select table_name, 2020 , concat('                do_method(dto)') from v_definition_table_base_list

	union all select table_name, 2021 , concat('    def check_all(self, check_method: Callable[[', table_name, '_write_dto], bool]) -> bool:') from v_definition_table_base_list
	union all select table_name, 2022 , concat('        init = True') from v_definition_table_base_list
	union all select table_name, 2023 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2024 , concat('            init = init and check_method(dto)') from v_definition_table_base_list
	union all select table_name, 2025 , concat('        return False') from v_definition_table_base_list

	union all select table_name, 2031 , concat('    def check_any(self, check_method: Callable[[', table_name, '_write_dto], bool]) -> bool:') from v_definition_table_base_list
	union all select table_name, 2032 , concat('        init = False') from v_definition_table_base_list
	union all select table_name, 2033 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2034 , concat('            init = init or check_method(dto)') from v_definition_table_base_list
	union all select table_name, 2035 , concat('        return False') from v_definition_table_base_list

	union all select table_name, 2041 , concat('    def map_to_string(self, map_method: Callable[[', table_name, '_write_dto], str]) -> list[str]:') from v_definition_table_base_list
	union all select table_name, 2042 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list
	union all select table_name, 2043 , concat('    def map_to_int(self, map_method: Callable[[', table_name, '_write_dto], int]) -> list[int]:') from v_definition_table_base_list
	union all select table_name, 2044 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list
	union all select table_name, 2045 , concat('    def map_to_float(self, map_method: Callable[[', table_name, '_write_dto], float]) -> list[float]:') from v_definition_table_base_list
	union all select table_name, 2046 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list

	union all select table_name, 2051 , concat('    def aggregate_string(self, map_method: Callable[[str, ', table_name, '_write_dto], str], init: str = "") -> str:') from v_definition_table_base_list
	union all select table_name, 2052 , concat('        init_value = init') from v_definition_table_base_list
	union all select table_name, 2053 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2054 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
	union all select table_name, 2055 , concat('        return init_value') from v_definition_table_base_list

	union all select table_name, 2061 , concat('    def aggregate_int(self, map_method: Callable[[int, ', table_name, '_write_dto], int], init: int = 0) -> int:') from v_definition_table_base_list
	union all select table_name, 2062 , concat('        init_value = init') from v_definition_table_base_list
	union all select table_name, 2063 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2064 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
	union all select table_name, 2065 , concat('        return init_value') from v_definition_table_base_list

	union all select table_name, 2071 , concat('    def aggregate_float(self, map_method: Callable[[float, ', table_name, '_write_dto], float], init: float = 0) -> float:') from v_definition_table_base_list
	union all select table_name, 2072 , concat('        init_value = init') from v_definition_table_base_list
	union all select table_name, 2073 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2074 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
	union all select table_name, 2075 , concat('        return init_value') from v_definition_table_base_list

	union all select table_name, 2101 , concat('    def filter(self, filter_method: Callable[[', table_name, '_write_dto], bool]) -> ', table_name, '_write_dtos:') from v_definition_table_base_list
	union all select table_name, 2102 , concat('        return ', table_name, '_write_dtos(list(filter(filter_method, self.dtos)))') from v_definition_table_base_list

	union all select table_name, 2111 , concat('    def group_by(self, group_method: Callable[[', table_name, '_write_dto], str]) -> dict[str, ', table_name, '_write_dtos]:') from v_definition_table_base_list
	union all select table_name, 2112 , concat('        grp_data: dict[str, ', table_name, '_write_dtos] = {}') from v_definition_table_base_list
	union all select table_name, 2113 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2114 , concat('            key = group_method(dto)') from v_definition_table_base_list
	union all select table_name, 2115 , concat('            grp_list = grp_data[key]') from v_definition_table_base_list
	union all select table_name, 2116 , concat('            if grp_list is None:') from v_definition_table_base_list
	union all select table_name, 2117 , concat('                grp_list = ', table_name, '_write_dtos([])') from v_definition_table_base_list
	union all select table_name, 2118 , concat('                grp_data[key] = grp_list') from v_definition_table_base_list
	union all select table_name, 2119 , concat('            grp_list.dtos.append(dto)') from v_definition_table_base_list
	union all select table_name, 2120 , concat('        return grp_data') from v_definition_table_base_list

	union all select table_name, 2131 , concat('    def aggregate_by(self, group_method: Callable[[', table_name, '_write_dto], str], agg_method: Callable[[', table_name, '_write_dtos], any]) -> dict[str, any]:') from v_definition_table_base_list
	union all select table_name, 2132 , concat('        grp_data: dict[str, ', table_name, '_write_dtos] = self.group_by(group_method)') from v_definition_table_base_list
	union all select table_name, 2133 , concat('        res: dict[str, any] = {}') from v_definition_table_base_list
	union all select table_name, 2134 , concat('        for key in grp_data:') from v_definition_table_base_list
	union all select table_name, 2135 , concat('            value = agg_method(grp_data[key])') from v_definition_table_base_list
	union all select table_name, 2136 , concat('            res[key] = value') from v_definition_table_base_list
	union all select table_name, 2137 , concat('        return res') from v_definition_table_base_list

	union all select table_name, 2201 , concat('    def find(self, check_method: Callable[[', table_name, '_write_dto], bool]) -> ', table_name, '_write_dto | None:') from v_definition_table_base_list
	union all select table_name, 2202 , concat('        for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2203 , concat('            if check_method(dto):') from v_definition_table_base_list
	union all select table_name, 2204 , concat('                return dto') from v_definition_table_base_list
	union all select table_name, 2205 , concat('        return None') from v_definition_table_base_list

	union all select table_name, 2301 , concat('    def compare_by(self, value_method: Callable[[', table_name, '_write_dto], any], compare_method: Callable[[any, any], bool]) -> ', table_name, '_write_dto | None:') from v_definition_table_base_list
	union all select table_name, 2302 , concat('        if len(self.dtos) == 0:') from v_definition_table_base_list
	union all select table_name, 2303 , concat('            return None') from v_definition_table_base_list
	union all select table_name, 2304 , concat('        else:') from v_definition_table_base_list
	union all select table_name, 2305 , concat('            max_value = value_method(self.dtos[0])') from v_definition_table_base_list
	union all select table_name, 2306 , concat('            max_elem = self.dtos[0]') from v_definition_table_base_list
	union all select table_name, 2307 , concat('            for dto in self.dtos:') from v_definition_table_base_list
	union all select table_name, 2308 , concat('                next_value = value_method(dto)') from v_definition_table_base_list
	union all select table_name, 2309 , concat('                if compare_method(next_value, max_value):') from v_definition_table_base_list
	union all select table_name, 2310 , concat('                    max_value = next_value') from v_definition_table_base_list
	union all select table_name, 2311 , concat('                    max_elem = dto') from v_definition_table_base_list
	union all select table_name, 2312 , concat('            return max_elem') from v_definition_table_base_list


	union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
	union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
	union all select 'zzzzzzzzzzzzzzzz' as table_name, 99999 as ordinal_position, '# auto-generated - v_definition_python_dtos_full - END' as python
) x order by x.table_name, x.ordinal_position
;



-- -------------------------------- full_dtos classes list: T_full_dtos
create or replace view v_definition_python_dtos_full_list as
select x.table_name, x.ordinal_position, x.python
from (
	select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_full_list - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'from __future__ import annotations'
	union all select '' as table_name, 3 as ordinal_position, 'from datetime import datetime'
	union all select '' as table_name, 4 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 5 as ordinal_position, 'from dataclasses import dataclass'
	union all select '' as table_name, 6 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos_thin import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_write import *'
	union all select '' as table_name, 9 as ordinal_position, 'from dto.dtos_read import *'
	union all select '' as table_name, 10 as ordinal_position, 'from dto.dtos_full import *'
	union all select '' as table_name, 11 as ordinal_position, 'import datetime'
	union all select '' as table_name, 12 as ordinal_position, 'from typing import Dict, Callable'
	union all select '' as table_name, 13 as ordinal_position, ''
	union all select '' as table_name, 14 as ordinal_position, ''

	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_full_dtos(base_dtos):') as python from v_definition_table_base_list
union all select table_name, 210 , concat('    dtos: list[', table_name , '_full_dto]') from v_definition_table_base_list
union all select table_name, 220 , concat('    def __init__(self, dtos: list[', table_name , '_full_dto]):') from v_definition_table_base_list

union all select table_name, 230 , '        super().__init__(dtos)' from v_definition_table_base_list
union all select table_name, 231 , '        self.dtos = dtos' from v_definition_table_base_list

union all select table_name, 300 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 301 , '    def empty_list(cls):' from v_definition_table_base_list
union all select table_name, 302 , '        return cls(list())' from v_definition_table_base_list

union all select table_name, 310 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 311 , concat('    def from_list(cls, dtos: list[', table_name , '_full_dto]):') from v_definition_table_base_list
union all select table_name, 312 , '        return cls(dtos)' from v_definition_table_base_list

union all select table_name, 320 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 321 , concat('    def from_object(cls, dto: ', table_name , '_full_dto):') from v_definition_table_base_list
union all select table_name, 322 , '        return cls([dto])' from v_definition_table_base_list

union all select table_name, 330 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 331 , concat('    def from_lists(cls, dtos1: list[', table_name , '_full_dto], dtos2: list[', table_name , '_full_dto]):') from v_definition_table_base_list
union all select table_name, 332 , '        return cls(dtos1 + dtos2)' from v_definition_table_base_list

union all select table_name, 551 , concat('    def find_by_uid(self, uid: str) -> ', table_name, '_full_dto | None:') from v_definition_table_base_list
union all select table_name, 552 , concat('        found_dtos = list(filter(lambda x: x.', table_name, '_uid == uid, self.dtos))') from v_definition_table_base_list
union all select table_name, 553 , concat('        if (len(found_dtos)>0):') from v_definition_table_base_list
union all select table_name, 554 , concat('            return found_dtos[0]') from v_definition_table_base_list
union all select table_name, 555 , concat('        else:') from v_definition_table_base_list
union all select table_name, 556 , concat('            return None') from v_definition_table_base_list

union all select table_name, 561 , concat('    def map_by_uid(self) -> dict[str, ', table_name , '_full_dto]:') from v_definition_table_base_list
union all select table_name, 562 , concat('        res = {}') from v_definition_table_base_list
union all select table_name, 563 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 564 , concat('            res[dto.', table_name , '_uid] = dto') from v_definition_table_base_list
union all select table_name, 565 , concat('        return res') from v_definition_table_base_list

union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
	union all select 'zzzzzzzzzzzzzzzz' as table_name, 99999 as ordinal_position, '# auto-generated - v_definition_python_dtos_full - END' as python
) x order by x.table_name, x.ordinal_position
;


-- -------------------------------- rich_dtos classes list: T_rich_dtos
create or replace view v_definition_python_dtos_rich_list as
select x.table_name, x.ordinal_position, x.python
from (
select '' as table_name, 1 as ordinal_position, concat('# auto-generated - v_definition_python_dtos_full_list - START at ', cast(now() as text)) as python
	union all select '' as table_name, 2 as ordinal_position, 'from __future__ import annotations'
	union all select '' as table_name, 3 as ordinal_position, 'from datetime import datetime'
	union all select '' as table_name, 4 as ordinal_position, 'from abc import abstractmethod'
	union all select '' as table_name, 5 as ordinal_position, 'from dataclasses import dataclass'
	union all select '' as table_name, 6 as ordinal_position, 'from dto.dtos import *'
	union all select '' as table_name, 7 as ordinal_position, 'from dto.dtos_thin import *'
	union all select '' as table_name, 8 as ordinal_position, 'from dto.dtos_write import *'
	union all select '' as table_name, 9 as ordinal_position, 'from dto.dtos_read import *'
	union all select '' as table_name, 10 as ordinal_position, 'from dto.dtos_full import *'
	union all select '' as table_name, 11 as ordinal_position, 'import datetime'
	union all select '' as table_name, 12 as ordinal_position, 'from typing import Dict, Callable'
	union all select '' as table_name, 13 as ordinal_position, ''
	union all select '' as table_name, 14 as ordinal_position, ''

	union all select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_rich_dtos(base_dtos):') as python from v_definition_table_base_list
union all select table_name, 210 , concat('    dtos: list[', table_name , '_rich_dto]') from v_definition_table_base_list
union all select table_name, 220 , concat('    def __init__(self, dtos: list[', table_name , '_rich_dto]):') from v_definition_table_base_list
union all select table_name, 230 , '        super().__init__(dtos)' from v_definition_table_base_list
union all select table_name, 231 , '        self.dtos = dtos' from v_definition_table_base_list

union all select table_name, 300 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 301 , '    def empty_list(cls):' from v_definition_table_base_list
union all select table_name, 302 , '        return cls(list())' from v_definition_table_base_list

union all select table_name, 310 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 311 , concat('    def from_list(cls, dtos: list[', table_name , '_rich_dto]):') from v_definition_table_base_list
union all select table_name, 312 , '        return cls(dtos)' from v_definition_table_base_list

union all select table_name, 320 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 321 , concat('    def from_object(cls, dto: ', table_name , '_rich_dto):') from v_definition_table_base_list
union all select table_name, 322 , '        return cls([dto])' from v_definition_table_base_list

union all select table_name, 330 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 331 , concat('    def from_lists(cls, dtos1: list[', table_name , '_rich_dto], dtos2: list[', table_name , '_rich_dto]):') from v_definition_table_base_list
union all select table_name, 332 , '        return cls(dtos1 + dtos2)' from v_definition_table_base_list

union all select table_name, 451 , concat('    def find_by_uid(self, uid: str) -> ', table_name, '_rich_dto | None:') from v_definition_table_base_list
union all select table_name, 452 , concat('        found_dtos = list(filter(lambda x: x.', table_name, '_uid == uid, self.dtos))') from v_definition_table_base_list
union all select table_name, 453 , concat('        if (len(found_dtos)>0):') from v_definition_table_base_list
union all select table_name, 454 , concat('            return found_dtos[0]') from v_definition_table_base_list
union all select table_name, 455 , concat('        else:') from v_definition_table_base_list
union all select table_name, 456 , concat('            return None') from v_definition_table_base_list

union all select table_name, 461 , concat('    def map_by_uid(self) -> dict[str, ', table_name , '_rich_dto]:') from v_definition_table_base_list
union all select table_name, 462 , concat('        res = {}') from v_definition_table_base_list
union all select table_name, 463 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 464 , concat('            res[dto.', table_name , '_uid] = dto') from v_definition_table_base_list
union all select table_name, 465 , concat('        return res') from v_definition_table_base_list

union all select table_name, 501 , concat('    def get_active(self) -> ', table_name, '_rich_dtos:') from v_definition_table_base_list
union all select table_name, 502 , concat('        return ', table_name, '_rich_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))') from v_definition_table_base_list

union all select table_name, 511 , concat('    def get_inactive(self) -> ', table_name, '_rich_dtos:') from v_definition_table_base_list
union all select table_name, 512 , concat('        return ', table_name, '_rich_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))') from v_definition_table_base_list

union all select table_name, 1001 , concat('    def get_first(self) -> ', table_name, '_rich_dto | None:') from v_definition_table_base_list
union all select table_name, 1002 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
union all select table_name, 1003 , concat('            return self.dtos[0]') from v_definition_table_base_list
union all select table_name, 1004 , concat('        else:') from v_definition_table_base_list
union all select table_name, 1005 , concat('            return None') from v_definition_table_base_list

union all select table_name, 1011 , concat('    def get_first_n(self, n: int) -> ', table_name, '_rich_dtos:') from v_definition_table_base_list
union all select table_name, 1012 , concat('        if len(self.dtos) > n:') from v_definition_table_base_list
union all select table_name, 1013 , concat('            return ', table_name, '_rich_dtos(self.dtos[:n])') from v_definition_table_base_list
union all select table_name, 1014 , concat('        else:') from v_definition_table_base_list
union all select table_name, 1015 , concat('            return ', table_name, '_rich_dtos(self.dtos)') from v_definition_table_base_list

union all select table_name, 1021 , concat('    def get_last(self) -> ', table_name, '_rich_dto | None:') from v_definition_table_base_list
union all select table_name, 1022 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
union all select table_name, 1023 , concat('            return self.dtos[-1]') from v_definition_table_base_list
union all select table_name, 1024 , concat('        else:') from v_definition_table_base_list
union all select table_name, 1025 , concat('            return None') from v_definition_table_base_list

union all select table_name, 1091 , concat('    def to_dict_by_uid(self) -> dict[str, ', table_name, '_rich_dto]:') from v_definition_table_base_list
union all select table_name, 1092 , concat('        d = {}') from v_definition_table_base_list
union all select table_name, 1093 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 1094 , concat('            d[dto.get_uid()] = dto') from v_definition_table_base_list
union all select table_name, 1095 , concat('        return d') from v_definition_table_base_list

union all select table_name, 2011 , concat('    def for_each(self, do_method: Callable):') from v_definition_table_base_list
union all select table_name, 2012 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2013 , concat('            do_method(dto)') from v_definition_table_base_list

union all select table_name, 2014 , concat('    def for_first(self, do_method: Callable):') from v_definition_table_base_list
union all select table_name, 2015 , concat('        if len(self.dtos) > 0:') from v_definition_table_base_list
union all select table_name, 2016 , concat('            return do_method(self.dtos[0])') from v_definition_table_base_list

union all select table_name, 2017 , concat('    def for_filter(self, check_method: Callable[[', table_name, '_rich_dto], bool], do_method: Callable):') from v_definition_table_base_list
union all select table_name, 2018 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2019 , concat('            if check_method(dto):') from v_definition_table_base_list
union all select table_name, 2020 , concat('                do_method(dto)') from v_definition_table_base_list

union all select table_name, 2021 , concat('    def check_all(self, check_method: Callable[[', table_name, '_rich_dto], bool]) -> bool:') from v_definition_table_base_list
union all select table_name, 2022 , concat('        init = True') from v_definition_table_base_list
union all select table_name, 2023 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2024 , concat('            init = init and check_method(dto)') from v_definition_table_base_list
union all select table_name, 2025 , concat('        return False') from v_definition_table_base_list

union all select table_name, 2031 , concat('    def check_any(self, check_method: Callable[[', table_name, '_rich_dto], bool]) -> bool:') from v_definition_table_base_list
union all select table_name, 2032 , concat('        init = False') from v_definition_table_base_list
union all select table_name, 2033 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2034 , concat('            init = init or check_method(dto)') from v_definition_table_base_list
union all select table_name, 2035 , concat('        return False') from v_definition_table_base_list

union all select table_name, 2041 , concat('    def map_to_string(self, map_method: Callable[[', table_name, '_rich_dto], str]) -> list[str]:') from v_definition_table_base_list
union all select table_name, 2042 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list
union all select table_name, 2043 , concat('    def map_to_int(self, map_method: Callable[[', table_name, '_rich_dto], int]) -> list[int]:') from v_definition_table_base_list
union all select table_name, 2044 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list
union all select table_name, 2045 , concat('    def map_to_float(self, map_method: Callable[[', table_name, '_rich_dto], float]) -> list[float]:') from v_definition_table_base_list
union all select table_name, 2046 , concat('        return list(map(lambda dto:  map_method(dto), self.dtos))') from v_definition_table_base_list

union all select table_name, 2051 , concat('    def aggregate_string(self, map_method: Callable[[str, ', table_name, '_rich_dto], str], init: str = "") -> str:') from v_definition_table_base_list
union all select table_name, 2052 , concat('        init_value = init') from v_definition_table_base_list
union all select table_name, 2053 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2054 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
union all select table_name, 2055 , concat('        return init_value') from v_definition_table_base_list

union all select table_name, 2061 , concat('    def aggregate_int(self, map_method: Callable[[int, ', table_name, '_rich_dto], int], init: int = 0) -> int:') from v_definition_table_base_list
union all select table_name, 2062 , concat('        init_value = init') from v_definition_table_base_list
union all select table_name, 2063 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2064 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
union all select table_name, 2065 , concat('        return init_value') from v_definition_table_base_list

union all select table_name, 2071 , concat('    def aggregate_float(self, map_method: Callable[[float, ', table_name, '_rich_dto], float], init: float = 0) -> float:') from v_definition_table_base_list
union all select table_name, 2072 , concat('        init_value = init') from v_definition_table_base_list
union all select table_name, 2073 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2074 , concat('            init_value = map_method(init_value, dto)') from v_definition_table_base_list
union all select table_name, 2075 , concat('        return init_value') from v_definition_table_base_list

union all select table_name, 2101 , concat('    def filter(self, filter_method: Callable[[', table_name, '_rich_dto], bool]) -> ', table_name, '_rich_dtos:') from v_definition_table_base_list
union all select table_name, 2102 , concat('        return ', table_name, '_rich_dtos(list(filter(filter_method, self.dtos)))') from v_definition_table_base_list

union all select table_name, 2111 , concat('    def group_by(self, group_method: Callable[[', table_name, '_rich_dto], str]) -> dict[str, ', table_name, '_rich_dtos]:') from v_definition_table_base_list
union all select table_name, 2112 , concat('        grp_data: dict[str, ', table_name, '_rich_dtos] = {}') from v_definition_table_base_list
union all select table_name, 2113 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2114 , concat('            key = group_method(dto)') from v_definition_table_base_list
union all select table_name, 2115 , concat('            grp_list = grp_data[key]') from v_definition_table_base_list
union all select table_name, 2116 , concat('            if grp_list is None:') from v_definition_table_base_list
union all select table_name, 2117 , concat('                grp_list = ', table_name, '_rich_dtos([])') from v_definition_table_base_list
union all select table_name, 2118 , concat('                grp_data[key] = grp_list') from v_definition_table_base_list
union all select table_name, 2119 , concat('            grp_list.dtos.append(dto)') from v_definition_table_base_list
union all select table_name, 2120 , concat('        return grp_data') from v_definition_table_base_list

union all select table_name, 2131 , concat('    def aggregate_by(self, group_method: Callable[[', table_name, '_rich_dto], str], agg_method: Callable[[', table_name, '_rich_dtos], any]) -> dict[str, any]:') from v_definition_table_base_list
union all select table_name, 2132 , concat('        grp_data: dict[str, ', table_name, '_rich_dtos] = self.group_by(group_method)') from v_definition_table_base_list
union all select table_name, 2133 , concat('        res: dict[str, any] = {}') from v_definition_table_base_list
union all select table_name, 2134 , concat('        for key in grp_data:') from v_definition_table_base_list
union all select table_name, 2135 , concat('            value = agg_method(grp_data[key])') from v_definition_table_base_list
union all select table_name, 2136 , concat('            res[key] = value') from v_definition_table_base_list
union all select table_name, 2137 , concat('        return res') from v_definition_table_base_list

union all select table_name, 2201 , concat('    def find(self, check_method: Callable[[', table_name, '_rich_dto], bool]) -> ', table_name, '_rich_dto | None:') from v_definition_table_base_list
union all select table_name, 2202 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2203 , concat('            if check_method(dto):') from v_definition_table_base_list
union all select table_name, 2204 , concat('                return dto') from v_definition_table_base_list
union all select table_name, 2205 , concat('        return None') from v_definition_table_base_list

union all select table_name, 2301 , concat('    def compare_by(self, value_method: Callable[[', table_name, '_rich_dto], any], compare_method: Callable[[any, any], bool]) -> ', table_name, '_rich_dto | None:') from v_definition_table_base_list
union all select table_name, 2302 , concat('        if len(self.dtos) == 0:') from v_definition_table_base_list
union all select table_name, 2303 , concat('            return None') from v_definition_table_base_list
union all select table_name, 2304 , concat('        else:') from v_definition_table_base_list
union all select table_name, 2305 , concat('            max_value = value_method(self.dtos[0])') from v_definition_table_base_list
union all select table_name, 2306 , concat('            max_elem = self.dtos[0]') from v_definition_table_base_list
union all select table_name, 2307 , concat('            for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 2308 , concat('                next_value = value_method(dto)') from v_definition_table_base_list
union all select table_name, 2309 , concat('                if compare_method(next_value, max_value):') from v_definition_table_base_list
union all select table_name, 2310 , concat('                    max_value = next_value') from v_definition_table_base_list
union all select table_name, 2311 , concat('                    max_elem = dto') from v_definition_table_base_list
union all select table_name, 2312 , concat('            return max_elem') from v_definition_table_base_list

union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
) x order by x.table_name, x.ordinal_position
;



-- -------------------------------- thin_dtos classes list: T_thin_dtos
create or replace view v_definition_thin_dtos as
select x.table_name, x.ordinal_position, x.python
from (
select table_name, 100 as ordinal_position, '@dataclass(frozen=False)' as python from v_definition_table_base_list
union all select table_name, 110 as ordinal_position, concat('class ', table_name , '_thin_dtos(base_dtos):') as python from v_definition_table_base_list
union all select table_name, 210 , concat('    dtos: list[', table_name , '_thin_dto]') from v_definition_table_base_list
union all select table_name, 220 , concat('    def __init__(self, dtos: list[', table_name , '_thin_dto]):') from v_definition_table_base_list
union all select table_name, 230 , '        super().__init__(dtos)' from v_definition_table_base_list
union all select table_name, 231 , '        self.dtos = dtos' from v_definition_table_base_list

union all select table_name, 300 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 301 , '    def empty_list(cls):' from v_definition_table_base_list
union all select table_name, 302 , '        return cls(list())' from v_definition_table_base_list

union all select table_name, 310 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 311 , concat('    def from_list(cls, dtos: list[', table_name , '_thin_dto]):') from v_definition_table_base_list
union all select table_name, 312 , '        return cls(dtos)' from v_definition_table_base_list

union all select table_name, 320 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 321 , concat('    def from_object(cls, dto: ', table_name , '_thin_dto):') from v_definition_table_base_list
union all select table_name, 322 , '        return cls([dto])' from v_definition_table_base_list

union all select table_name, 330 , '    @classmethod' from v_definition_table_base_list
union all select table_name, 331 , concat('    def from_lists(cls, dtos1: list[', table_name , '_thin_dto], dtos2: list[', table_name , '_thin_dto]):') from v_definition_table_base_list
union all select table_name, 332 , '        return cls(dtos1 + dtos2)' from v_definition_table_base_list

union all select table_name, 551 , concat('    def find_by_uid(self, uid: str) -> ', table_name, '_thin_dto | None:') from v_definition_table_base_list
union all select table_name, 552 , concat('        found_dtos = list(filter(lambda x: x.', table_name, '_uid == uid, self.dtos))') from v_definition_table_base_list
union all select table_name, 553 , concat('        if len(found_dtos)>0:') from v_definition_table_base_list
union all select table_name, 554 , concat('            return found_dtos[0]') from v_definition_table_base_list
union all select table_name, 555 , concat('        else:') from v_definition_table_base_list
union all select table_name, 556 , concat('            return None') from v_definition_table_base_list

union all select table_name, 561 , concat('    def map_by_uid(self) -> dict[str, ', table_name , '_thin_dto]:') from v_definition_table_base_list
union all select table_name, 562 , concat('        res = {}') from v_definition_table_base_list
union all select table_name, 563 , concat('        for dto in self.dtos:') from v_definition_table_base_list
union all select table_name, 564 , concat('            res[dto.', table_name , '_uid] = dto') from v_definition_table_base_list
union all select table_name, 565 , concat('        return res') from v_definition_table_base_list

union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
) x order by x.table_name, x.ordinal_position
;






-- -------------------------------- dao classes: T_dao
create or replace view v_definition_dao_base as
select x.table_name, x.ordinal_position, x.python
from (
select table_name, 1000 as ordinal_position, concat('class ', table_name, '_dao(base_dao):') as python from v_definition_table_base_list
union all select table_name, 1001 , concat('    def __init__(self):') from v_definition_table_base_list
union all select table_name, 1002 , concat('        super().__init__()') from v_definition_table_base_list
union all select table_name, 1003 , concat('    def get_model(self) -> base_model:') from v_definition_table_base_list
union all select table_name, 1004 , concat('        return db_models.', table_name, '_model') from v_definition_table_base_list

union all select table_name, 1010 , concat('    def select_rows_read_by_query(self, sql: str, params: Iterable = []) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 1011 , concat('        return ', table_name, '_read_dtos(list(map(lambda r: ', table_name, '_read_dto(*r), self.get_objects(sql, params))))') from v_definition_table_base_list

union all select table_name, 1021 , concat('    def select_rows_write_by_query(self, sql: str, params: Iterable = []) -> ', table_name, '_write_dtos:') from v_definition_table_base_list
union all select table_name, 1022 , concat('        return ', table_name, '_write_dtos(list(map(lambda r: ', table_name, '_write_dto(*r), self.get_objects(sql, params))))') from v_definition_table_base_list

union all select table_name, 1031 , concat('    def select_rows_thin_by_query(self, sql: str, params: Iterable = []) -> ', table_name, '_thin_dtos:') from v_definition_table_base_list
union all select table_name, 1032 , concat('        return ', table_name, '_thin_dtos(list(map(lambda r: ', table_name, '_thin_dto(*r), self.get_objects(sql, params))))') from v_definition_table_base_list

union all select table_name, 1041 , concat('    def select_rows_rich_by_query(self, sql: str, params: Iterable = []) -> ', table_name, '_write_dtos:') from v_definition_table_base_list
union all select table_name, 1042 , concat('        return ', table_name, '_write_dtos(list(map(lambda r: ', table_name, '_write_dto(*r), self.get_objects(sql, params))))') from v_definition_table_base_list

union all select table_name, 1051 , concat('    def select_row_first_by_query(self, sql: str, params: Iterable = []) -> ', table_name, '_read_dto | None:') from v_definition_table_base_list
union all select table_name, 1052 , concat('        return self.select_rows_read_by_query(sql, params).get_first()') from v_definition_table_base_list

union all select table_name, 1061 , concat('    def select_rows_read_order_by_column(self, col_name: str, params: Iterable = [], n: int = 1000) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 1062 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_order_by_query(col_name, n), params)') from v_definition_table_base_list

union all select table_name, 1071 , concat('    def select_rows_read_all(self, n: int = 1000) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 1072 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_all_limit_sql(n))') from v_definition_table_base_list

union all select table_name, 1075 , concat('    def select_rows_read_active(self, n: int = 1000) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 1076 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_active_limit_sql(n))') from v_definition_table_base_list

union all select table_name, 1081 , concat('    def select_rows_read_all_latest(self, n: int = 1000) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 1082 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_all_latest_sql(n))') from v_definition_table_base_list

union all select table_name, 1091 , concat('    def select_rows_read_active_latest(self, n: int = 1000) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 1092 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_active_latest_sql(n))') from v_definition_table_base_list

union all select table_name, 1111 , concat('    def select_rows_write_all(self, n: int = 1000) -> ', table_name, '_write_dtos:') from v_definition_table_base_list
union all select table_name, 1112 , concat('        return self.select_rows_write_by_query(self.get_model().get_select_write_all_limit_sql(n))') from v_definition_table_base_list

union all select table_name, 1121 , concat('    def select_rows_write_active(self, n: int = 1000) -> ', table_name, '_write_dtos:') from v_definition_table_base_list
union all select table_name, 1122 , concat('        return self.select_rows_write_by_query(self.get_model().get_select_write_active_limit_sql(n))') from v_definition_table_base_list

union all select table_name, 1131 , concat('    def select_rows_write_all_latest(self, n: int = 1000) -> ', table_name, '_write_dtos:') from v_definition_table_base_list
union all select table_name, 1132 , concat('        return self.select_rows_write_by_query(self.get_model().get_select_write_all_latest_sql(n))') from v_definition_table_base_list

union all select table_name, 1141 , concat('    def select_rows_write_active_latest(self, n: int = 1000) -> ', table_name, '_write_dtos:') from v_definition_table_base_list
union all select table_name, 1142 , concat('        return self.select_rows_write_by_query(self.get_model().get_select_write_active_latest_sql(n))') from v_definition_table_base_list

union all select table_name, 1151 , concat('    def select_row_read_by_uid(self, uid: str) -> ', table_name, '_read_dto | None:') from v_definition_table_base_list
union all select table_name, 1152 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_by_key(), (uid,)).get_first()') from v_definition_table_base_list

union all select table_name, 1161 , concat('    def select_row_read_by_id(self, id: int) -> ', table_name, '_read_dto | None:') from v_definition_table_base_list
union all select table_name, 1162 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_by_id(), (id,)).get_first()') from v_definition_table_base_list

union all select table_name, 1171 , concat('    def select_rows_read_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 1172 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,))') from v_definition_table_base_list

union all select table_name, 1181 , concat('    def select_rows_read_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 1182 , concat('        return self.select_rows_read_by_query(self.get_model().get_select_active_by_any_column_values(col_name, col_values, n), col_values)') from v_definition_table_base_list

union all select table_name, 1191 , concat('    def select_rows_thin_all(self, n: int = 1000) -> ', table_name, '_thin_dtos:') from v_definition_table_base_list
union all select table_name, 1192 , concat('        return self.select_rows_thin_by_query(self.get_model().get_select_thin_all_sql(n))') from v_definition_table_base_list

union all select table_name, 1301+ordinal_position*10 , concat('    def select_rows_read_by_', column_name, '(self, ', python_definition, ', n: int = 1000) -> ', table_name, '_read_dtos:') from v_column_list where is_attribute=1
union all select table_name, 1302+ordinal_position*10 , concat('        return self.select_rows_read_by_any_column(''', column_name,''', ', column_name, ', n)') from v_column_list where is_attribute=1

union all select table_name, 4401 , concat('    def insert_dto(self, dto: ', table_name, '_write_dto, created_by: str = objects.created_by_default) -> int:') from v_definition_table_base_list
union all select table_name, 4402 , concat('        return self.insert_single(dto, created_by)') from v_definition_table_base_list

union all select table_name, 4430 as ordinal_position, concat('    def insert_row(self, ', attr_python_definition_defaults , ', created_by: str = objects.created_by_default) -> int:') as python from v_table_column
union all select table_name, 4431 as ordinal_position, concat('        return self.insert_single(', table_name, '_write_dto.new_write(', attr_column_list, '), created_by)') as python from v_table_column

union all select table_name, 4440 as ordinal_position, concat('    def insert_row_random_uid(self, ', attrnonkey_column_list_with_type , ', created_by: str = objects.created_by_default) -> int:') as python from v_table_column
union all select table_name, 4441 as ordinal_position, concat('        return self.insert_single(', table_name, '_write_dto.new_write_random_uid(', attrnonkey_column_list, '), created_by)') as python from v_table_column

union all select table_name, 4460 , concat('    def insert_dtos(self, dtos: list[', table_name, '_write_dto], created_by: str = objects.created_by_default) -> int:') from v_definition_table_base_list
union all select table_name, 4461 , concat('        return self.insert_many(dtos, created_by)') from v_definition_table_base_list

union all select table_name, 4470 , concat('    def insert_write_dtos(self, dtos: ', table_name, '_write_dtos, created_by: str = objects.created_by_default) -> int:') from v_definition_table_base_list
union all select table_name, 4471 , concat('        return self.insert_dtos(dtos.dtos, created_by)') from v_definition_table_base_list

union all select table_name, 4480 , concat('    def insert_read_dtos(self, dtos: ', table_name, '_read_dtos, created_by: str = objects.created_by_default) -> int:') from v_definition_table_base_list
union all select table_name, 4481 , concat('        return self.insert_dtos(dtos.get_write_dtos(), created_by)') from v_definition_table_base_list

union all select table_name, 4490 , concat('    def insert_and_get(self, dto: ' , table_name, '_write_dto, created_by: str = objects.created_by_default) -> ' , table_name, '_read_dto | None:') from v_definition_table_base_list
union all select table_name, 4491 , concat('        self.insert_single(dto, created_by)') from v_definition_table_base_list
union all select table_name, 4492 , concat('        return self.select_row_read_by_uid(dto.get_uid())') from v_definition_table_base_list

union all select table_name, 4495 , concat('    def insert_and_get_many(self, dtos: ', table_name, '_write_dtos, created_by: str = objects.created_by_default) -> ', table_name, '_read_dtos:') from v_definition_table_base_list
union all select table_name, 4496 , concat('        return ', table_name, '_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))') from v_definition_table_base_list

union all select table_name, 5530 as ordinal_position, concat('    def upsert_row(self, ', attr_column_list_with_type , ', updated_by: str=objects.created_by_default) -> int:') as python from v_table_column
union all select table_name, 5531 as ordinal_position, concat('        params = ', table_name, '_write_dto.new_write(', attr_column_list, ').get_list_write_insert(updated_by)') as python from v_table_column
union all select table_name, 5532 as ordinal_position, concat('        return self.execute_query(self.get_model().upsert_attrs_sql, params)') as python from v_table_column

union all select table_name, 5540 as ordinal_position, concat('    def upsert_row_and_get(self, ', attr_column_list_with_type , ', updated_by: str = objects.created_by_default) -> ', table_name, '_read_dto | None:') as python from v_table_column
union all select table_name, 5541 as ordinal_position, concat('        params = ', table_name, '_write_dto.new_write(', attr_column_list, ').get_list_write_insert(updated_by)') as python from v_table_column
union all select table_name, 5542 as ordinal_position, concat('        self.execute_query(self.get_model().upsert_attrs_sql, params)') as python from v_table_column
union all select table_name, 5543 as ordinal_position, concat('        return self.select_row_read_by_uid(', table_name, '_uid)') as python from v_table_column

union all select table_name, 6440 , concat('    def delete_logical_dtos(self, dtos: list[', table_name, '_write_dto], removed_by: str = objects.created_by_default) -> int:') from v_definition_table_base_list
union all select table_name, 6441 , concat('        uids = list(map(lambda dto: dto.get_uid(), dtos))') from v_definition_table_base_list
union all select table_name, 6442 , concat('        return self.delete_logical_by_uids(uids, removed_by)') from v_definition_table_base_list

union all select table_name, 6450 , concat('    def delete_logical_write_dtos(self, dtos: ', table_name, '_write_dtos, removed_by: str = objects.created_by_default) -> int:') from v_definition_table_base_list
union all select table_name, 6451 , concat('        return self.delete_logical_dtos(dtos.dtos, removed_by)') from v_definition_table_base_list

union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
) x order by x.table_name, x.ordinal_position
;


select * from (select *, row_number() over (partition by created_by order by last_updated_date desc) as row_num from account_group) x where x.row_num=1


union all select table_name, 1191 , concat('') from v_definition_table_base_list
union all select table_name, 1192 , concat('') from v_definition_table_base_list

union all select table_name, 1221 , concat('') from v_definition_table_base_list
union all select table_name, 1222 , concat('') from v_definition_table_base_list

union all select table_name, 1241 , concat('') from v_definition_table_base_list
union all select table_name, 1242 , concat('') from v_definition_table_base_list

union all select table_name, 1251 , concat('') from v_definition_table_base_list
union all select table_name, 1252 , concat('') from v_definition_table_base_list

union all select table_name, 1261 , concat('') from v_definition_table_base_list
union all select table_name, 1262 , concat('') from v_definition_table_base_list

union all select table_name, 1271 , concat('') from v_definition_table_base_list
union all select table_name, 1272 , concat('') from v_definition_table_base_list

union all select table_name, 1271 , concat('') from v_definition_table_base_list
union all select table_name, 1272 , concat('') from v_definition_table_base_list

union all select table_name, 1281 , concat('') from v_definition_table_base_list
union all select table_name, 1282 , concat('') from v_definition_table_base_list

union all select table_name, 1291 , concat('') from v_definition_table_base_list
union all select table_name, 1292 , concat('') from v_definition_table_base_list


union all select table_name, 1321 , concat('') from v_definition_table_base_list
union all select table_name, 1322 , concat('') from v_definition_table_base_list

union all select table_name, 1341 , concat('') from v_definition_table_base_list
union all select table_name, 1342 , concat('') from v_definition_table_base_list

union all select table_name, 1351 , concat('') from v_definition_table_base_list
union all select table_name, 1352 , concat('') from v_definition_table_base_list

union all select table_name, 1361 , concat('') from v_definition_table_base_list
union all select table_name, 1362 , concat('') from v_definition_table_base_list

union all select table_name, 1371 , concat('') from v_definition_table_base_list
union all select table_name, 1372 , concat('') from v_definition_table_base_list

union all select table_name, 1371 , concat('') from v_definition_table_base_list
union all select table_name, 1372 , concat('') from v_definition_table_base_list

union all select table_name, 1381 , concat('') from v_definition_table_base_list
union all select table_name, 1382 , concat('') from v_definition_table_base_list

union all select table_name, 1391 , concat('') from v_definition_table_base_list
union all select table_name, 1392 , concat('') from v_definition_table_base_list


-- -------------------------------- dao FULL classes
select x.table_name, x.ordinal_position, x.python
from (
select table_name, 1000 as ordinal_position, concat('class ', table_name, '_full_dao(', table_name, '_dao):') as python from v_definition_table_base_list
union all select table_name, 1001 , concat('    def __init__(self):') from v_definition_table_base_list
union all select table_name, 1002 , concat('        super().__init__()') from v_definition_table_base_list
union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
) x order by x.table_name, x.ordinal_position
;


-- -------------------------------- models
select table_name, 1 as ordinal_position, concat('    ', table_name, '_dao_instance = ', table_name,'_full_dao()') as python
from v_table_column
order by table_name
;

;


-- -------------------------------- DAOs registers
select table_name, 1 as ordinal_position, concat('        self.all_daos["', table_name, '_dao"] = self.', table_name, '_dao_instance') as python
from v_table_column
order by table_name
;


-- -------------------------------- services
select x.table_name, x.ordinal_position as ordinal_position, x.python
from (
select table_name, 1000 as ordinal_position, concat('class ', table_name, '_service(service_base):') as python from v_definition_table_base_list
union all select table_name, 1001 , concat('    dao: ', table_name , '_full_dao = daos.', table_name , '_dao_instance') from v_definition_table_base_list
union all select table_name, 1002 , concat('    def __init__(self):') from v_definition_table_base_list
union all select table_name, 1003 , concat('        super().__init__()') from v_definition_table_base_list
union all select table_name, 99900 , empty_line_definition from v_definition_table_base_list
union all select table_name, 99901 , empty_line_definition from v_definition_table_base_list
) x order by x.table_name, x.ordinal_position
;


-- -------------------------------- service instances

select table_name, 1 as ordinal_position, concat('    ', table_name, '_service_inst = ', table_name, '_service()') as python
from v_definition_table_base_list order by table_name





-- -------------------------------- service registers

select concat('        self.all_services.append(self.', table_name, '_service_inst)')
from v_definition_table_base_list
order by table_name






-- --------------------------------



        <sql splitStatements="false" stripComments="false">
            insert into system_version(system_version_uid, system_version_name, version_description)
            values ('1.0.0', '1.0.0', 'Initial version of application with all basic features.');
        </sql>

        <sql splitStatements="false" stripComments="false">
            insert into system_database(system_database_uid, system_database_name, db_url, db_host, db_name, db_user)
            values ('timetracker', 'timetracker', '', '', '', '');
        </sql>

        <sql splitStatements="false" stripComments="false">
            insert into system_instance(system_instance_uid, system_instance_name, system_version_uid, host_name, host_ip, local_path, mode_name)
            values ('1.0.0', '1.0.0', '1.0.0', '', '', '', 'PROD');
        </sql>

        <sql splitStatements="false" stripComments="false">
            insert into system_object_type(system_object_type_uid, system_object_type_name, object_type_description)
            values ( 'system', 'system', 'system');
            insert into system_object_type(system_object_type_uid, system_object_type_name, object_type_description)
            values ( 'dictionary', 'dictionary', 'dictionary');
            insert into system_object_type(system_object_type_uid, system_object_type_name, object_type_description)
            values ( 'data', 'data', 'data');
            insert into system_object_type(system_object_type_uid, system_object_type_name, object_type_description)
            values ( 'append', 'append', 'append');
            insert into system_object_type(system_object_type_uid, system_object_type_name, object_type_description)
            values ( 'm2m', 'm2m', 'm2m');
        </sql>

        <sql splitStatements="false" stripComments="false">
            insert into system_table(system_table_uid, system_table_name, key_name, table_comment)
            select t.table_name, t.table_name, concat(t.table_name, '_uid') as key_name, coalesce(tc.table_comment, '') as table_comment
            from information_schema.tables t
            	 left join (
				 SELECT t.table_name, pg_catalog.obj_description(pgc.oid, 'pg_class') as table_comment
					FROM information_schema.tables t
					INNER JOIN pg_catalog.pg_class pgc ON t.table_name = pgc.relname
					WHERE t.table_type='BASE TABLE'
					AND t.table_schema='public'
			 ) tc on t.table_name = tc.table_name
            WHERE t.table_type='BASE TABLE' and t.table_schema='public' and t.table_name not in ('databasechangeloglock', 'databasechangelog');
        </sql>

        <sql splitStatements="false" stripComments="false">
            insert into system_setting(system_setting_uid, system_setting_name, setting_value)
            values ('dao_max_rows', 'dao_max_rows', '1000');
            insert into system_setting(system_setting_uid, system_setting_name, setting_value)
            values ('db_pool_min_connections', 'db_pool_min_connections', '3');
            insert into system_setting(system_setting_uid, system_setting_name, setting_value)
            values ('db_pool_max_connections', 'db_pool_max_connections', '30');
            insert into system_setting(system_setting_uid, system_setting_name, setting_value)
            values ('system_email', 'system_email', '');
            insert into system_setting(system_setting_uid, system_setting_name, setting_value)
            values ('test_email', 'test_email', '');
            insert into system_setting(system_setting_uid, system_setting_name, setting_value)
            values ('administrator_email', 'administrator_email', '');
        </sql>

        <sql splitStatements="false" stripComments="false">
            insert into system_module(system_module_uid, system_module_name, system_module_description)
            values ('Main', 'Main', 'Main');
            insert into system_module(system_module_uid, system_module_name, system_module_description)
            values ('TimeTracking', 'TimeTracking', 'TimeTracking');
            insert into system_module(system_module_uid, system_module_name, system_module_description)
            values ('Calendar', 'Calendar', 'Calendar');
            insert into system_module(system_module_uid, system_module_name, system_module_description)
            values ('Invoice', 'Invoice', 'Invoice');
            insert into system_module(system_module_uid, system_module_name, system_module_description)
            values ('Project', 'Project', 'Project');
        </sql>

        <sql splitStatements="false" stripComments="false">
            insert into system_license(system_license_uid, system_license_name, license_description)
            values ('Full', 'Full', 'Full license with all features');
            insert into system_license(system_license_uid, system_license_name, license_description)
            values ('Test', 'Test', 'Test license with limited features to test application');
        </sql>
            insert into tenant(tenant_uid, country_uid, tenant_type_uid, tenant_category_uid, tenant_name, tenant_code, tenant_description, start_date, is_internal, is_system, is_test)
            values ('System', 'XX', 'System', 'Internal', 'system', 'system', 'System tenant - default one', now(), 1, 1, 0);
            insert into tenant(tenant_uid, country_uid, tenant_type_uid, tenant_category_uid, tenant_name, tenant_code, tenant_description, start_date, is_internal, is_system, is_test)
            values ('Test', 'XX', 'Test', 'Internal', 'test', 'test', 'Test tenant - just for testing purpose', now(), 1, 1, 1);

           insert into tenant_account(tenant_account_name, tenant_uid, account_uid, tenant_role_uid)
            values ('Assignment of Administrator role to system tenant', 'System', 'system', 'Administrator');
            insert into tenant_account(tenant_account_name, tenant_uid, account_uid, tenant_role_uid)
            values ('Assignment of Administrator role to system tenant', 'Test', 'test', 'Administrator');



































select dc.table_name, dc.column_name
from (
 select table_name, 'row_seq' as column_name
 from INFORMATION_SCHEMA.tables
 where table_type='BASE TABLE' and table_schema='public'
 ) dc
left join INFORMATION_SCHEMA.columns c on c.table_name=dc.table_name and c.column_name=dc.column_name
where c.column_name is null

connection_engine	system_lock_uid
storage_query	system_lock_uid
synchronization_type	system_lock_uid

period	system_lock_uid
calendar_type	system_lock_uid

connection_engine	owner_account_group_uid
storage_query	owner_account_group_uid
synchronization_type	owner_account_group_uid
period	owner_account_group_uid
calendar_type	owner_account_group_uid

invoice_action	row_seq


 left join  dc
 where
  and c.column_name='system_instance_uid'


select column_name, count(*) as cnt
from INFORMATION_SCHEMA.columns
where column_name in ('system_instance_uid', 'system_lock_uid', 'owner_account_group_uid', 'row_seq', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes')
group by column_name


select column_name, count(*) as cnt
from INFORMATION_SCHEMA.columns
where column_name in ('system_instance_uid', 'system_lock_uid', 'owner_account_group_uid', 'row_seq', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes')
group by column_name


            <column name="" type="text" defaultValue="1.0.0"><constraints nullable="false"/></column>
            <column name="" type="text" />
            <column name="" type="text" defaultValue="System"><constraints nullable="false"/></column>
            <column name="" type="bigint" autoIncrement="true"><constraints nullable="false"/></column>
            <column name="" type="text" remarks="global generated unique ID" defaultValueComputed="replace(concat('project_budget_v01_', substring(cast(now() as text), 1, 10), '_', substring(cast(uuid_generate_v4() as text), 1, 13)), '-', '_')"><constraints nullable="false"/></column>
            <column name="" type="bigint" defaultValueNumeric="0" remarks="version of the row"><constraints nullable="false"/></column>
            <column name="" type="bigint" defaultValueNumeric="1" remarks="0 - row has been logically deleted, 1 - row is still active"><constraints nullable="false"/></column>
            <column name="" type="timestamp" defaultValueDate="${nowdate}" remarks="date and time of insertion given row to database"><constraints nullable="false"/></column>
            <column name="" type="text" defaultValue="system" remarks="account UID of person that created this row"><constraints nullable="false"/></column>
            <column name="" type="timestamp" defaultValueDate="${nowdate}" remarks="date and time of last change of this row"><constraints nullable="false"/></column>
            <column name="" type="text" defaultValue="system" remarks="account UID of person that updated this row"><constraints nullable="false"/></column>
            <column name="" type="timestamp" remarks="date and time of change this row" />
            <column name="" type="text" remarks="account UID of person that removed this row" />
            <column name="" type="text" defaultValue="{}"><constraints nullable="false"/></column>




select cast(nextval('seq_id') as text)

CREATE or replace FUNCTION generate_uid(table_code text) RETURNS text as
$func$
BEGIN
	RETURN replace(concat('acc', '_', cast(nextval('seq_id') as text), '_', substring(cast(now() as text), 1, 10), '_', substring(cast(uuid_generate_v4() as text), 1, 13), ''), '-', '_');
END
$func$
LANGUAGE plpgsql;

select substring(cast(now() as text), 1, 10)

select generate_uid('aaa')

select replace(concat('acc', '_', substring(cast(now() as text), 1, 10), '_', substring(cast(uuid_generate_v4() as text), 1, 13), ''), '-', '_')


































































































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
union all select table_name, 1002 , concat('        logging.info("Starting ', table_name, ' DAO")') from v_table_list
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
