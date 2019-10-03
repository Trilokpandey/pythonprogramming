col_list=['city_id ','content_score ','n_images ','distance_to_center ','stars ','n_reviews','avg_price ','avg_saving_percent']



for i in range(0,len(col_list)):
    df[col_list[i]]=df[col_list[i]].fillna(df[col_list[i]].mode()[0])