select distinct translate((tipolog.descricao||' '||log.nome_logradouro) ,'âàãáÁÂÀÃéêÉÊíÍóôõÓÔÕüúÜÚÇç','AAAAAAAAEEEEIIOOOOOOUUUUCC') from sistema_viario.logradouro log
inner join sistema_viario.tipo_logradouro tipolog on log.id_tipo_logradouro = tipolog.id_tipo_logradouro
where log.ind_ativo = 'S'


select *  from sistema_viario.logradouro log 
where log.nome_logradouro = 'A'  and  log.ind_ativo = 'S'


select  distinct translate((tipolog.descricao||' '||log.nome_logradouro|| ' '||ende.numero_imovel||' '||bp.nome_bairro_popular||' '||re.nome_regional) ,'âàãáÁÂÀÃéêÉÊíÍóôõÓÔÕüúÜÚÇç','AAAAAAAAEEEEIIOOOOOOUUUUCC')  from sistema_viario.logradouro log 
inner join cadastro_tecnico.endereco_pbh ende on ende.id_logradouro = log.id_logradouro
inner join sistema_viario.tipo_logradouro tipolog on log.id_tipo_logradouro = tipolog.id_tipo_logradouro
inner join cadastro_tecnico.bairro_popular bp on bp.id_bairro_popular = ende.id_bairro_popular
inner join cadastro_tecnico.regional  re on re.id_regional = ende.id_regional
where log.ind_ativo = 'S'