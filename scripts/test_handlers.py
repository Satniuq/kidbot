def test_sim_sem_pending_choice():
    ctx = fake_ctx("sim")
    sim(ctx)
    assert ctx.response_type == "confirmado"
