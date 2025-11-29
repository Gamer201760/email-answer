#!/usr/bin/env python3
"""🔥 BM25 RAG - БЕЗ haystack/elasticsearch!"""
from rank_bm25 import BM25Okapi
import PyPDF2, os, json, pickle, sys
from pathlib import Path

def read_pdf(filepath):
    """Читает PDF → текст"""
    try:
        text = ""
        with open(filepath, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text.strip()
    except:
        return ""

def create_bm25_index(docs_path="./rules/"):
    """📚 Индексация PDF → BM25"""
    if not os.path.exists(docs_path):
        print(f"❌ Создай папку: mkdir -p {docs_path}")
        return
    
    chunks, sources = [], []
    pdf_files = [f for f in os.listdir(docs_path) if f.endswith('.pdf')]
    print(f"📁 Найдено PDF: {pdf_files}")
    
    for pdf_file in pdf_files:
        filepath = os.path.join(docs_path, pdf_file)
        print(f"\n📄 Обрабатываю {pdf_file}...")
        text = read_pdf(filepath)
        print(f"📏 {len(text):,} символов, {len(text.split())} слов")
        
        # Чанки по 100 слов
        words = text.split()
        for i in range(0, len(words), 100):
            chunk = ' '.join(words[i:i+100])
            if len(chunk.split()) >= 20:
                chunks.append(chunk)
                sources.append(pdf_file)
                print(f"   ✅ Чанк #{len(chunks)} ({len(chunk.split())} слов)")
    
    print(f"\n✂️ ИТОГО: {len(chunks)} чанков из {len(pdf_files)} PDF")
    
    if chunks:
        tokenized = [c.lower().split() for c in chunks]
        bm25 = BM25Okapi(tokenized)
        
        # 💾 СОХРАНЕНИЕ
        data = {'chunks': chunks, 'sources': sources}
        Path("bm25_index.json").write_text(json.dumps(data, ensure_ascii=False, indent=2))
        with open("bm25_model.pkl", "wb") as f:
            pickle.dump(bm25, f)
        
        print("✅ 🎉 BM25 INDEX СОЗДАН!")
    else:
        print("❌ Нет текста в PDF")

def get_context(query, k=3):
    """🔍 Поиск по запросу"""
    try:
        data = json.loads(Path("bm25_index.json").read_text(encoding='utf-8'))
        with open("bm25_model.pkl", "rb") as f:
            bm25 = pickle.load(f)
        
        scores = bm25.get_scores(query.lower().split())
        top_k = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:k]
        
        context = []
        for i, score in top_k:
            if score > 0:  # 🔧 ПОНИЗИЛ ПОРОГ С 0.1 → 0
                chunk = data['chunks'][i][:500] + "..."
                context.append(f"📄 {data['sources'][i]}\n{chunk}\n(score: {score:.2f})")
        
        return "\n\n".join(context) if context else f"❌ Нет документов по запросу '{query}'"
    except FileNotFoundError:
        return "❌ Сначала: python3 -m rag.rag index"
    except Exception as e:
        return f"❌ Ошибка: {e}"


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "index":
        create_bm25_index()
    elif len(sys.argv) > 1 and sys.argv[1] == "test":
        print("🧪 ТЕСТ БАНКОВСКИХ ПИСЕМ:")
        print(get_context("надежный клиент"))
    else:
        print("🚀 RAG BM25 - ТЕСТ БАНКОВСКИХ ДОКУМЕНТОВ:")
        print(get_context("письмо банка"))
        print("\n📋 КОМАНДЫ:")
        print("   python3 -m rag.rag index         # Индексация")
        print("   python3 -m rag.rag test          # Тест")
        print("   python3 -c 'from rag.rag import get_context; print(get_context(\"текущий счет\"))'")

