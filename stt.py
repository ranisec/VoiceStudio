import os, sys
# 보안: 캐시된 모델만 사용, huggingface.co 접속 차단 (새 모델 받을 땐 HF_HUB_OFFLINE=0)
os.environ.setdefault("HF_HUB_OFFLINE","1")
os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY","1")
from faster_whisper import WhisperModel
m=WhisperModel(sys.argv[2] if len(sys.argv)>2 else "small",device="cpu",compute_type="int8")
segs,info=m.transcribe(sys.argv[1],language="ko",vad_filter=True)
for s in segs: print(f"[{s.start:.1f}-{s.end:.1f}] {s.text}")
