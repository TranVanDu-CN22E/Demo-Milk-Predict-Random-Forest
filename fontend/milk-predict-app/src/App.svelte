<script>
  import { fade, slide } from 'svelte/transition';

  // Khởi tạo các biến dữ liệu form
  let pH = 7.0;
  let Temprature = 25.0;
  let Taste = 0;
  let Odor = 0;
  let Fat = 0;
  let Turbidity = 0;
  let Colour = 255;

  let result = null; // Sẽ nhận cấu trúc: { "prediction": 0, "grade": "Low" }
  let loading = false;
  let error = null;

  // Hàm chuyển đổi checkbox (0 hoặc 1)
  const toggleValue = (val) => (val === 1 ? 0 : 1);

  // Hàm định dạng tên kết quả hiển thị
  function getGradeText(grade) {
    if (!grade) return '';
    const upper = grade.toUpperCase();
    if (upper === 'HIGH') return 'Chất Lượng Cao (High)';
    if (upper === 'MEDIUM') return 'Chất Lượng Vừa (Medium)';
    return 'Chất Lượng Thấp (Low)';
  }

  async function handleSubmit() {
    loading = true;
    error = null;
    result = null;

    const payload = { pH, Temprature, Taste, Odor, Fat, Turbidity, Colour };

    try {
      const response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (!response.ok) throw new Error('Không thể kết nối đến máy chủ backend.');
      result = await response.json();
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }
</script>

<div class="page-wrapper">
  <main class="card">
    <header class="header">
      <h2>Hệ Thống Phân Tích & Dự Đoán Chất Lượng</h2>
      <p class="subtitle">Nhập các chỉ số đo lường thực tế để kiểm tra</p>
    </header>

    <form on:submit|preventDefault={handleSubmit} class="form">
      <!-- Hàng 1: pH và Nhiệt độ -->
      <div class="row">
        <div class="form-group">
          <label for="ph">Độ pH: <span class="badge ph-badge">{pH}</span></label>
          <input type="range" id="ph" min="0" max="14" step="0.1" bind:value={pH} />
          <div class="range-labels"><span>0 (Axit)</span><span>7 (Trung tính)</span><span>14 (Kiềm)</span></div>
        </div>

        <div class="form-group">
          <label for="temp">Nhiệt độ (°C)</label>
          <input type="number" id="temp" step="0.1" bind:value={Temprature} placeholder="Ví dụ: 35.0" />
        </div>
      </div>

      <!-- Hàng 2: Màu sắc -->
      <div class="form-group">
        <label for="colour">Mã màu sắc (Colour: 0 - 255)</label>
        <div class="color-input-wrapper">
          <input type="number" id="colour" min="0" max="255" bind:value={Colour} />
          <div class="color-preview" style="background-color: rgb({Colour}, {Colour}, {Colour})"></div>
        </div>
      </div>

      <!-- Hàng 3: Các thuộc tính chọn nhanh -->
      <div class="form-group">
        <label class="section-label">Các thuộc tính kiểm thử</label>
        <div class="grid-checkbox">
          <label class="chip-checkbox" class:active={Taste === 1}>
            <input type="checkbox" checked={Taste === 1} on:change={() => Taste = toggleValue(Taste)} />
            <span class="icon">✨</span> Vị ngon (Taste)
          </label>

          <label class="chip-checkbox" class:active={Odor === 1}>
            <input type="checkbox" checked={Odor === 1} on:change={() => Odor = toggleValue(Odor)} />
            <span class="icon">👃</span> Có mùi (Odor)
          </label>

          <label class="chip-checkbox" class:active={Fat === 1}>
            <input type="checkbox" checked={Fat === 1} on:change={() => Fat = toggleValue(Fat)} />
            <span class="icon">🧈</span> Độ béo (Fat)
          </label>

          <label class="chip-checkbox" class:active={Turbidity === 1}>
            <input type="checkbox" checked={Turbidity === 1} on:change={() => Turbidity = toggleValue(Turbidity)} />
            <span class="icon">🌫️</span> Độ đục (Turbidity)
          </label>
        </div>
      </div>

      <!-- Nút bấm Gửi lệnh -->
      <button type="submit" class="btn-submit" disabled={loading}>
        {#if loading}
          <span class="spinner"></span> Đang phân tích dữ liệu...
        {:else}
          Bắt Đầu Phân Tích Đánh Giá
        {/if}
      </button>
    </form>

    <!-- Khối hiển thị Lỗi -->
    {#if error}
      <div class="alert error-alert" transition:slide>
        <span class="alert-icon">⚠️</span>
        <div class="alert-content">
          <h4>Phát sinh lỗi kết nối</h4>
          <p>{error}</p>
        </div>
      </div>
    {/if}

    <!-- Khối kết quả ĐẸP XUẤT SẮC -->
    {#if result}
      <div class="result-card state-{result.grade?.toLowerCase()}" transition:fade>
        <div class="result-header">
          <span class="status-indicator"></span>
          <h3>KẾT QUẢ PHÂN TÍCH</h3>
        </div>
        
        <div class="result-body">
          <div class="main-grade">
            <span class="grade-label">Đánh giá chung:</span>
            <h1 class="grade-value">{getGradeText(result.grade)}</h1>
          </div>
          
          <div class="meta-info">
            <div class="meta-item">
              <span class="meta-label">Mã định danh dự đoán (Prediction)</span>
              <span class="meta-val badge-index">{result.prediction}</span>
            </div>
          </div>
        </div>
      </div>
    {/if}
  </main>
</div>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    min-height: 100vh;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #333;
  }

  .page-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px 20px;
    min-height: 80vh;
  }

  .card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    border-radius: 24px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.5);
    width: 100%;
    max-width: 680px;
    padding: 35px;
    box-sizing: border-box;
  }

  .header {
    text-align: center;
    margin-bottom: 30px;
  }

  .logo-icon {
    font-size: 3rem;
    margin-bottom: 10px;
  }

  .header h2 {
    margin: 0 0 8px 0;
    font-size: 1.6rem;
    color: #1a202c;
    font-weight: 700;
  }

  .subtitle {
    margin: 0;
    color: #718096;
    font-size: 0.95rem;
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }

  @media (max-width: 480px) {
    .row { grid-template-columns: 1fr; }
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #4a5568;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .section-label {
    margin-bottom: 4px;
  }

  .badge {
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: bold;
  }

  .ph-badge {
    background: #e2e8f0;
    color: #2d3748;
  }

  input[type="number"] {
    padding: 12px 16px;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    font-size: 1rem;
    outline: none;
    transition: all 0.2s;
    background: #fff;
  }

  input[type="number"]:focus {
    border-color: #4f46e5;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
  }

  input[type="range"] {
    width: 100%;
    height: 6px;
    background: #e2e8f0;
    border-radius: 5px;
    outline: none;
    margin: 10px 0;
  }

  .range-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.75rem;
    color: #a0aec0;
  }

  .color-input-wrapper {
    display: flex;
    gap: 12px;
    align-items: center;
  }

  .color-input-wrapper input {
    flex: 1;
  }

  .color-preview {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    border: 2px solid #e2e8f0;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
    transition: background-color 0.2s;
  }

  .grid-checkbox {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  .chip-checkbox {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 16px;
    background: #fff;
    border: 2px solid #e2e8f0;
    border-radius: 14px;
    cursor: pointer;
    user-select: none;
    transition: all 0.2s ease;
    font-weight: 500;
  }

  .chip-checkbox input {
    display: none;
  }

  .chip-checkbox:hover {
    border-color: #cbd5e1;
    background: #f8fafc;
  }

  .chip-checkbox.active {
    background: #e0e7ff;
    border-color: #4f46e5;
    color: #4338ca;
  }

  .icon {
    font-size: 1.1rem;
  }

  .btn-submit {
    margin-top: 10px;
    padding: 16px;
    background: #4f46e5;
    color: white;
    border: none;
    border-radius: 14px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    transition: all 0.2s ease;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
  }

  .btn-submit:hover:not(:disabled) {
    background: #4338ca;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4);
  }

  .btn-submit:active:not(:disabled) {
    transform: translateY(0);
  }

  .btn-submit:disabled {
    background: #94a3b8;
    box-shadow: none;
    cursor: not-allowed;
  }

  /* Hiệu ứng loading quay tròn */
  .spinner {
    width: 20px;
    height: 20px;
    border: 3px solid rgba(255,255,255,0.3);
    border-radius: 50%;
    border-top-color: white;
    animation: spin 0.8s linear infinite;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  /* Khối thông báo lỗi */
  .alert {
    margin-top: 25px;
    padding: 16px;
    border-radius: 14px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .error-alert {
    background: #fef2f2;
    border: 1px solid #fee2e2;
    color: #991b1b;
  }

  .alert-icon { font-size: 1.3rem; }
  .alert-content h4 { margin: 0 0 4px 0; font-size: 0.95rem; font-weight: 700; }
  .alert-content p { margin: 0; font-size: 0.85rem; opacity: 0.9; }/* KHỐI KẾT QUẢ CỰC ĐẸP */.result-card {margin-top: 30px;border-radius: 20px;padding: 24px;border: 1px solid transparent;transition: all 0.3s ease;}.result-header {display: flex;align-items: center;gap: 10px;margin-bottom: 16px;border-bottom: 1px solid rgba(0,0,0,0.06);padding-bottom: 10px;}.result-header h3 {margin: 0;font-size: 0.9rem;letter-spacing: 0.05em;font-weight: 700;}.status-indicator {width: 10px;height: 10px;border-radius: 50%;display: inline-block;}.grade-label {font-size: 0.85rem;color: #64748b;display: block;margin-bottom: 4px;}.grade-value {margin: 0;font-size: 1.8rem;font-weight: 800;}.meta-info {margin-top: 18px;padding-top: 14px;border-top: 1px dashed rgba(0,0,0,0.08);}.meta-item {display: flex;justify-content: space-between;align-items: center;font-size: 0.9rem;}.meta-label { color: #64748b; }.badge-index {background: rgba(0,0,0,0.06);color: #334155;padding: 4px 10px;border-radius: 8px;font-weight: 600;}/* Biến đổi màu sắc UI theo từng cấp độ kết quả trả về từ Backend */.state-high {background: #f0fdf4;border-color: #bbf7d0;color: #166534;}.state-high .status-indicator { background: #22c55e; animation: pulse 2s infinite; }.state-high .result-header h3 { color: #166534; }.state-medium {background: #fffbeb;border-color: #fef3c7;color: #92400e;}.state-medium .status-indicator { background: #f59e0b; }.state-medium .result-header h3 { color: #92400e; }.state-low {background: #fef2f2;border-color: #fee2e2;color: #991b1b;}.state-low .status-indicator { background: #ef4444; }.state-low .result-header h3 { color: #991b1b; }@keyframes pulse {0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(34, 197, 94, 0); }100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }}</style>