## The following code is part of the program sla_report_qr.py. Some sensitive and unnecessary parts of the program are omitted.

import pandas as pd

writer_cbd = create_writer(excel_file_type="CBD")
writer_ctf = create_writer(excel_file_type="CTF")


sql_qr_cbd = read_sql_file(config['sla_report_qr']['sql_file_path_cbd'])
sql_qr_ctf = read_sql_file(config['sla_report_qr']['sql_file_path_ctf'])


# ## CBD
# df_qr_raw_cbd = pd.DataFrame().append(pd.read_sql(sql = sql_qr_cbd, con=engine, params=[period[0], period[1]]))
# df_qr_raw_cbd_selected = df_qr_raw_cbd[['cargo_type', 'meet_sla', 'late_handover']].copy().reset_index(drop=True).rename(
# 	columns={'cargo_type': 'Cargo Type', 'meet_sla': 'SLA Met', 'late_handover': 'Late Handover'})
# ## Add a column containing 1 for counting to the right of the DF.
# df_qr_raw_cbd_selected['Counts of AWB'] = 1
# ## pandas.pivot_table() returns a 'pandas.core.frame.DataFrame' object.
# ## aggfunc=lambda x: len(x) and aggfunc=sum give the same result.
# df_qr_cbd_sum_table = pd.pivot_table(df_qr_raw_cbd_selected, values='Counts of AWB', index=['Cargo Type', 'SLA Met'],
# 									 columns=['Late Handover'], fill_value=0, aggfunc=sum, margins=True, margins_name='Total')
# cargo_list = list(df_qr_cbd_sum_table.index.get_level_values(0).unique())
# cargo_list.remove('Total')
# sum_table_cbd = pd.concat([df_qr_cbd_sum_table,
#            df_qr_cbd_sum_table.loc[cargo_list].sum(level=[0]).assign(meet_sla = 'Sub Total').set_index('meet_sla', append=True)]).sort_index(level=[0,1])
# print("Summary table:", sum_table_cbd, sep="\n")
#
# ## CTF
# df_qr_raw_ctf = pd.DataFrame().append(pd.read_sql(sql = sql_qr_ctf, con=engine, params=[period[0], period[1]]))
# df_qr_raw_ctf_selected = df_qr_raw_ctf[['trf_type', 'meet_sla', 'late_handover']].copy().reset_index(drop=True).rename(
# 	columns={'trf_type': 'TRF Type', 'meet_sla': 'SLA Met', 'late_handover': 'Late Handover'})
# ## Add a column containing 1 for counting to the right of the DF.
# df_qr_raw_ctf_selected['Counts of AWB'] = 1
# ## pandas.pivot_table() returns a 'pandas.core.frame.DataFrame' object.
# ## aggfunc=lambda x: len(x) and aggfunc=sum give the same result.
# df_qr_ctf_sum_table = pd.pivot_table(df_qr_raw_ctf_selected, values='Counts of AWB', index=['TRF Type', 'SLA Met'],
# 									 columns=['Late Handover'], fill_value=0, aggfunc=sum, margins=True, margins_name='Total')
# trf_list = list(df_qr_ctf_sum_table.index.get_level_values(0).unique())
# trf_list.remove('Total')
# sum_table_ctf = pd.concat([df_qr_ctf_sum_table,
#            df_qr_ctf_sum_table.loc[trf_list].sum(level=[0]).assign(meet_sla = 'Sub Total').set_index('meet_sla', append=True)]).sort_index(level=[0,1])
# print("Summary table:", sum_table_ctf, sep="\n")

def summarize_data(sql_qr, selected_cols, renamed_cols, pivot_table_index):
	## period[0] is a string like 20200301
	## period[1] is a string like 20200401
	df_qr_raw = pd.DataFrame().append(pd.read_sql(sql=sql_qr, con=engine, params=[period[0], period[1]]))
	df_qr_raw_selected = df_qr_raw[selected_cols].copy().reset_index(drop=True).rename(
		columns=renamed_cols)
	## Add a column containing 1 for counting to the right of the DF.
	df_qr_raw_selected['Counts of AWB'] = 1
	## pandas.pivot_table() returns a 'pandas.core.frame.DataFrame' object.
	## aggfunc=lambda x: len(x) and aggfunc=sum give the same result.
	df_qr_sum_table = pd.pivot_table(df_qr_raw_selected, values='Counts of AWB', index=pivot_table_index,
										 columns=['Late Handover'], fill_value=0, aggfunc=sum, margins=True,
										 margins_name='Total')
	loc_list = list(df_qr_sum_table.index.get_level_values(0).unique())
	loc_list.remove('Total')
	sum_table = pd.concat([df_qr_sum_table,
							   df_qr_sum_table.loc[loc_list].sum(level=[0]).assign(meet_sla='Sub Total').set_index('meet_sla', append=True)]).sort_index(level=[0, 1])
	print("Summary table:", sum_table, sep="\n")
	return sum_table, df_qr_raw

selected_cols_cbd = ['cargo_type', 'meet_sla', 'late_handover']
renamed_cols_cbd = {'cargo_type': 'Cargo Type', 'meet_sla': 'SLA Met', 'late_handover': 'Late Handover'}
pivot_table_index_cbd = ['Cargo Type', 'SLA Met']
sum_table_cbd, df_qr_raw_cbd = summarize_data(sql_qr=sql_qr_cbd, selected_cols=selected_cols_cbd,
											  renamed_cols=renamed_cols_cbd, pivot_table_index=pivot_table_index_cbd)

selected_cols_ctf = ['trf_type', 'meet_sla', 'late_handover']
renamed_cols_ctf = {'trf_type': 'TRF Type', 'meet_sla': 'SLA Met', 'late_handover': 'Late Handover'}
pivot_table_index_ctf = ['TRF Type', 'SLA Met']
sum_table_ctf, df_qr_raw_ctf = summarize_data(sql_qr=sql_qr_ctf, selected_cols=selected_cols_ctf,
											  renamed_cols=renamed_cols_ctf, pivot_table_index=pivot_table_index_ctf)

# ## CBD
# ## Write the summary table to Excel
# sum_table_cbd.to_excel(writer_cbd, sheet_name="QR_SLA_CBD_Summary", header=True, index=True, startrow=1, startcol=0)
# ## Add 'Counts of AWB' to cell A1
# pd.DataFrame(['Counts of AWB']).to_excel(writer_cbd, sheet_name="QR_SLA_CBD_Summary", header=False, index=False, startrow=0, startcol=0)
# ## Write all raw data from sql_qr_cbd
# df_qr_raw_cbd.to_excel(writer_cbd, sheet_name="QR_SLA_CBD_Raw", header=True, index=False, startrow=0, startcol=0)
#
# ## CTF
# ## Write the summary table to Excel
# sum_table_ctf.to_excel(writer_ctf, sheet_name="QR_SLA_CTF_Summary", header=True, index=True, startrow=1, startcol=0)
# ## Add 'Counts of AWB' to cell A1
# pd.DataFrame(['Counts of AWB']).to_excel(writer_ctf, sheet_name="QR_SLA_CTF_Summary", header=False, index=False, startrow=0, startcol=0)
# ## Write all raw data from sql_qr_ctf
# df_qr_raw_ctf.to_excel(writer_ctf, sheet_name="QR_SLA_CTF_Raw", header=True, index=False, startrow=0, startcol=0)


def write_df_to_excel(sum_table, writer, excel_file_type, df_qr_raw):
	## Write the summary table to Excel
	sum_table.to_excel(writer, sheet_name="QR_SLA_{}_Summary".format(excel_file_type), header=True, index=True, startrow=1, startcol=0)
	## Add 'Counts of AWB' to cell A1
	pd.DataFrame(['Counts of AWB']).to_excel(writer, sheet_name="QR_SLA_{}_Summary".format(excel_file_type), header=False, index=False, startrow=0, startcol=0)
	## Write all raw data from sql_qr_cbd
	df_qr_raw.to_excel(writer, sheet_name="QR_SLA_{}_Raw".format(excel_file_type), header=True, index=False, startrow=0, startcol=0)

write_df_to_excel(sum_table=sum_table_cbd, writer=writer_cbd, excel_file_type="CBD", df_qr_raw=df_qr_raw_cbd)
write_df_to_excel(sum_table=sum_table_ctf, writer=writer_ctf, excel_file_type="CTF", df_qr_raw=df_qr_raw_ctf)
