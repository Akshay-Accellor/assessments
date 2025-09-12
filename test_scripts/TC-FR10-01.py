Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-10: Rollout Completion by Deadline', () => {
    before(async () => { await browser.url('http://www.ipsy.com/admin/status'); });
    it('Positive - Verify the rollout is completed by the deadline', async () => {
        const status = await $('.rollout-status');
        await expect(status).toHaveText('Completed');
        const transitionCheck = await $('.transition-check');
        await expect(transitionCheck).toHaveText('Successful');
    });
    it('Negative - Verify status if rollout incomplete', async () => {
        const status = await $('.rollout-status');
        await expect(status).not.toHaveText('Completed');
    });
    it('Edge - Verify exactly on deadline date', async () => {
        const deadlineDate = await $('.deadline-date');
        await expect(deadlineDate).toHaveText('2025-02-28');
        const status = await $('.rollout-status');
        await expect(status).toHaveText('Completed');
    });
});
