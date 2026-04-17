"""
Seed database with sample news articles for testing.
"""
from backend.database.db import db
from datetime import datetime, timedelta

def seed_articles():
    """Add sample articles to the database."""

    sample_articles = [
        {
            "title": "GPT-5 Rumors: What We Know About OpenAI's Next Big Model",
            "url": "https://techcrunch.com/2024/gpt-5-rumors",
            "summary": "Industry insiders suggest OpenAI is working on GPT-5 with significant improvements in reasoning and multimodal capabilities. Expected release timeline remains unclear.",
            "topic": "AI/ML",
            "published_date": (datetime.now() - timedelta(days=1)).isoformat()
        },
        {
            "title": "Google Gemini 2.0 Achieves Breakthrough in Code Generation",
            "url": "https://arstechnica.com/google-gemini-2-code",
            "summary": "Google's latest Gemini model shows remarkable improvements in generating production-ready code, outperforming previous benchmarks by 40%.",
            "topic": "AI/ML",
            "published_date": (datetime.now() - timedelta(days=2)).isoformat()
        },
        {
            "title": "AWS Announces Graviton4: 30% Better Performance for Cloud Workloads",
            "url": "https://aws.amazon.com/blogs/graviton4-launch",
            "summary": "Amazon Web Services unveils Graviton4 processors, promising significant cost savings and performance improvements for cloud-native applications.",
            "topic": "Cloud/DevOps",
            "published_date": (datetime.now() - timedelta(days=1)).isoformat()
        },
        {
            "title": "Kubernetes 1.30 Released with Enhanced Security Features",
            "url": "https://kubernetes.io/blog/2024/release-1-30",
            "summary": "The latest Kubernetes release focuses on improved security policies, better observability, and simplified cluster management capabilities.",
            "topic": "Cloud/DevOps",
            "published_date": (datetime.now() - timedelta(days=3)).isoformat()
        },
        {
            "title": "React 19 Brings Concurrent Features to Production",
            "url": "https://react.dev/blog/2024/react-19-release",
            "summary": "React 19 officially stabilizes concurrent rendering, server components, and automatic batching for improved performance and developer experience.",
            "topic": "Web Development",
            "published_date": (datetime.now() - timedelta(days=2)).isoformat()
        },
        {
            "title": "Next.js 15 Introduces Partial Prerendering and Turbopack",
            "url": "https://nextjs.org/blog/next-15",
            "summary": "Vercel launches Next.js 15 with groundbreaking partial prerendering capabilities and the stable release of Turbopack for faster builds.",
            "topic": "Web Development",
            "published_date": (datetime.now() - timedelta(days=1)).isoformat()
        },
        {
            "title": "Flutter 4.0: Cross-Platform Development Gets Major Upgrade",
            "url": "https://flutter.dev/blog/flutter-4-announcement",
            "summary": "Google releases Flutter 4.0 with improved performance, better desktop support, and enhanced integration with native platform features.",
            "topic": "Mobile",
            "published_date": (datetime.now() - timedelta(days=2)).isoformat()
        },
        {
            "title": "Swift 6.0 Brings Strict Concurrency Checking",
            "url": "https://swift.org/blog/swift-6-released",
            "summary": "Apple's Swift 6.0 introduces comprehensive concurrency safety features, helping developers catch race conditions at compile time.",
            "topic": "Mobile",
            "published_date": (datetime.now() - timedelta(days=4)).isoformat()
        },
        {
            "title": "Critical Zero-Day Vulnerability Found in Popular npm Package",
            "url": "https://thehackernews.com/2024/npm-zero-day",
            "summary": "Security researchers discover a critical vulnerability in a widely-used npm package affecting millions of Node.js applications worldwide.",
            "topic": "Security",
            "published_date": (datetime.now() - timedelta(days=1)).isoformat()
        },
        {
            "title": "New AI-Powered Threat Detection System Stops Ransomware in Real-Time",
            "url": "https://www.darkreading.com/ai-ransomware-defense",
            "summary": "Cybersecurity firm unveils AI system that can detect and neutralize ransomware attacks within milliseconds using behavioral analysis.",
            "topic": "Security",
            "published_date": (datetime.now() - timedelta(days=2)).isoformat()
        },
        {
            "title": "PyTorch 2.2 Introduces Native Distributed Training Support",
            "url": "https://pytorch.org/blog/pytorch-2-2-release",
            "summary": "Meta releases PyTorch 2.2 with built-in distributed training capabilities, making it easier to train large-scale machine learning models.",
            "topic": "Data Science",
            "published_date": (datetime.now() - timedelta(days=3)).isoformat()
        },
        {
            "title": "Pandas 3.0: Major Performance Improvements for Data Analysis",
            "url": "https://pandas.pydata.org/blog/pandas-3-announcement",
            "summary": "The popular Python data analysis library gets a major upgrade with 10x faster operations and improved memory efficiency.",
            "topic": "Data Science",
            "published_date": (datetime.now() - timedelta(days=1)).isoformat()
        },
    ]

    for article in sample_articles:
        try:
            db.add_article(
                title=article["title"],
                url=article["url"],
                summary=article["summary"],
                topic=article["topic"],
                published_date=article["published_date"]
            )
            print(f"✓ Added: {article['title']}")
        except Exception as e:
            print(f"✗ Error adding article: {e}")

    print(f"\n✓ Successfully seeded {len(sample_articles)} articles!")

if __name__ == "__main__":
    seed_articles()
