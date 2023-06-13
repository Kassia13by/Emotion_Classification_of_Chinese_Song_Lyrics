# Emotion_Classification_of_Chinese_Song_Lyrics

該專案主題是針對魔境歌詞網歌詞資料，隨機選取 4020 首歌，利用語言學特徵進行歌詞情感分類。 
本資料夾結構如下：
```bash
├── Emotion_Classification_of_Chinese_Song_Lyrics
│   ├── cleaning.ipynb
│   ├── create_lyrics_word_embeddings.ipynb
│   ├── feature_extraction.ipynb
│   ├── model_training.ipynb
│   ├── tokenize_labeled_lyrics.py
│   └── tokenize_rest_lyrics_for_embeddings.py
│   ├── data
│   │   ├── Glove_CNA_ASBC_300d.txt
│   │   ├── LIWC.csv
│   │   ├── cleaned_result.csv
│   │   ├── filtered_combined_data.csv
│   │   ├── final.csv
│   │   ├── final_all.csv
│   │   ├── text_label_data.csv
│   │   ├── tokenized_labeled_lyrics.csv
│   │   ├── tokenized_rest_lyrics_for_embeddings.csv
│   │   └── word_embeddings.txt
│   └── 
└── 
```
## 檔案說明

### Emotion_Classification_of_Chinese_Song_Lyrics

cleaning.ipynb：前處理時使用之檔案，清除「作詞：、作曲：」等無關內容

create_lyrics_word_embeddings.ipynb：利用 115636 首中文歌曲自製歌詞的詞嵌入（word embeddings）

feature_extraction.ipynb：手動抓取語言學特徵之檔案（可以直接讀入 text_label_data.csv 使用）

model_training.ipynb：模型訓練所在之檔案（可以直接讀入 final_all.csv 使用）

tokenize_labeled_lyrics.py：使用 CKIP 為已標記之歌詞（4020 首）進行斷詞之檔案

tokenize_rest_lyrics_for_embeddings.py：使用 CKIP 為其餘非 4020 首之歌詞進行斷詞檔案，為自製歌詞詞嵌入使用

#### data：本專案使用之資料所在資料夾

Glove_CNA_ASBC_300d.txt：CKIP GloVe 之詞嵌入，可於 [CKIP Lab 中文詞知識庫小組| 中文向量表達 - 中央研究院](https://ckip.iis.sinica.edu.tw/project/embedding) 下載（由於版權及檔案過大問題，在此不附上）

LIWC.csv：LIWC 中文詞典（用於抓取情緒相關詞彙特徵）

cleaned_result.csv：使用 cleaning.ipynb 清理過後欲進行斷詞之檔案

filtered_combined_data.csv：扣除已標記之 4020 首歌之檔案，欲進行詞嵌入製作使用（由於檔案過大問題，在此不附上）

final.csv：欲使用 cleaning.ipynb 清理之檔案

final_all.csv：包含清理、斷詞、標記、特徵等此專案所需資料之最終內容

text_label_data.csv：包含標記和斷詞之檔案

tokenized_labeled_lyrics.csv：4020 首已標記之歌詞斷詞檔案

tokenized_rest_lyrics_for_embeddings.csv：4020 首已標記之歌詞以外之所有歌曲斷詞檔案

word_embeddings.txt：自製歌詞詞嵌入（由於檔案過大問題，在此不附上）
